import copy
import json
import os
import sys

from PySide6.QtCore import QEvent, Qt, QTimer
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QSpinBox,
    QVBoxLayout,
)

from .lib import Font, Glyph, json_to_font, font_to_json
from .ui_mainwindow import Ui_MainWindow
from .ui_characterpreview import Ui_Dialog

DEFAULT_GLYPHS = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    ".", ",", ":", "'", "-", " ",
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.font: Font | None = None
        self.current_glyph: Glyph | None = None
        self.current_file: str | None = None

        self.undo_stack: list[tuple[Glyph, list]] = []
        self.redo_stack: list[tuple[Glyph, list]] = []

        self.autosave_timer = QTimer(self)
        self.autosave_timer.setSingleShot(True)
        self.autosave_timer.setInterval(300)
        self.autosave_timer.timeout.connect(self.autosave)

        QShortcut(QKeySequence.StandardKey.Undo, self).activated.connect(
            self.undo_drawing
        )
        QShortcut(QKeySequence.StandardKey.Redo, self).activated.connect(
            self.redo_drawing
        )

        self.ui.glyphCanvas.installEventFilter(self)

    def eventFilter(self, watched, event):
        if watched is self.ui.glyphCanvas:
            if event.type() == QEvent.Type.MouseButtonPress:
                self.remember_drawing_state()
            elif event.type() == QEvent.Type.MouseButtonRelease:
                self.schedule_autosave()

        return super().eventFilter(watched, event)

    def refresh_font_controls(self):
        if self.font is None:
            return

        self.ui.fontNameBox.setText(self.font.name)
        self.ui.fontHeightBox.setValue(self.font.height)
        self.ui.fontDefaultSpacingBox.setValue(self.font.default_spacing)
        self.ui.fontDefaultWidthBox.setValue(self.font.default_width)

        register_font_glyphs_to_window(self, self.font)
        selected_glyph(self, None)

    def schedule_autosave(self):
        if self.current_file is not None:
            self.autosave_timer.start()

    def autosave(self):
        if self.font is not None and self.current_file is not None:
            save_font_to_path(self, self.current_file, show_errors=False)

    def remember_drawing_state(self):
        if self.current_glyph is None:
            return

        self.undo_stack.append(
            (self.current_glyph, copy.deepcopy(self.current_glyph.grid))
        )
        self.redo_stack.clear()

    def undo_drawing(self):
        if not self.undo_stack:
            return

        glyph, previous_grid = self.undo_stack.pop()
        self.redo_stack.append((glyph, copy.deepcopy(glyph.grid)))
        glyph.grid = previous_grid

        if self.current_glyph is glyph:
            self.ui.glyphCanvas.update()

        self.schedule_autosave()

    def redo_drawing(self):
        if not self.redo_stack:
            return

        glyph, next_grid = self.redo_stack.pop()
        self.undo_stack.append((glyph, copy.deepcopy(glyph.grid)))
        glyph.grid = next_grid

        if self.current_glyph is glyph:
            self.ui.glyphCanvas.update()

        self.schedule_autosave()


def show_error(parent, title: str, message: str):
    message_box = QMessageBox(parent)
    message_box.setIcon(QMessageBox.Icon.Critical)
    message_box.setWindowTitle(title)
    message_box.setText(message)
    message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    message_box.exec()


def initialise_new_font() -> Font:
    font = Font("Default", 8)

    for character in DEFAULT_GLYPHS:
        Glyph(character, font.height, font)

    return font


def register_font_glyphs_to_window(window: MainWindow, font: Font) -> None:
    window.ui.glyphSelectorList.clear()

    # checklist logic used to be here but it broke
    # :-( lmao
    for glyph in font.glyphs:
        if glyph.blank:
             window.ui.glyphSelectorList.addItem(f"{glyph.name}")
        else:
             window.ui.glyphSelectorList.addItem(f"{glyph.name}")


def selected_glyph(window: MainWindow, glyph: Glyph | None):
    window.current_glyph = glyph

    if glyph is None:
        window.ui.selectedGlyphTitle.setText("No selected glyph")
        window.ui.identiferCharBox.clear()
        window.ui.glyphCanvas.glyph = None
        window.ui.glyphCanvas.update()
        return

    window.ui.selectedGlyphTitle.setText(f"Selected glyph: {glyph.name}")
    window.ui.identiferCharBox.setText(glyph.name)
    window.ui.widthBox.setValue(glyph.width)
    window.ui.glyphCanvas.glyph = glyph
    window.ui.glyphCanvas.update()


def get_glyph_from_name(font: Font | None, glyph_name: str) -> Glyph | None:
    if font is None:
        return None

    for glyph in font.glyphs:
        if glyph.name == glyph_name:
            return glyph

    return None


def save_font_to_path(
    window: MainWindow,
    file_path: str,
    show_errors: bool = True,
) -> bool:
    if window.font is None:
        return False

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(font_to_json(window.font))

        window.current_file = file_path
        window.setWindowTitle(
            f"{window.font.name} — {os.path.basename(file_path)}"
        )
        
        return True
    except (OSError, TypeError, ValueError) as error:
        if show_errors:
            show_error(window, "Could not save font", str(error))
        return False


def trigger_save(window: MainWindow):
    if window.current_file is None:
        trigger_save_to_new_file(window)
        return

    save_font_to_path(window, window.current_file)


def trigger_save_to_new_file(window: MainWindow):
    if window.font is None:
        return

    suggested_name = f"{window.font.name}.json"
    file_path, _ = QFileDialog.getSaveFileName(
        window,
        "Save font",
        suggested_name,
        "Font files (*.json);;All files (*)",
    )

    if not file_path:
        return

    if not file_path.lower().endswith(".json"):
        file_path += ".json"

    save_font_to_path(window, file_path)


def trigger_open(window: MainWindow):
    file_path, _ = QFileDialog.getOpenFileName(
        window,
        "Open font",
        "",
        "Font files (*.json);;All files (*)",
    )

    if not file_path:
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            opened_font = json_to_font(file.read())
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        show_error(
            window,
            "Could not open font",
            f"This is not a font file\n\n{error}",
        )
        return

    window.autosave_timer.stop()
    window.font = opened_font
    window.preview_ui.graphicsView.set_font(window.font)
    window.current_file = file_path
    window.undo_stack.clear()
    window.redo_stack.clear()
    window.refresh_font_controls()
    window.setWindowTitle(
        f"{opened_font.name} - {os.path.basename(file_path)}"
    )


def handle_font_name_edit(window: MainWindow, new_text: str):
    if window.font is None:
        return

    window.font.name = new_text
    window.schedule_autosave()


def handle_font_height_edit(window: MainWindow, new_value: int):
    if window.font is None:
        return

    window.font.height = new_value
    window.ui.glyphCanvas.update()
    window.schedule_autosave()


def handle_default_width_edit(window: MainWindow, new_value: int):
    if window.font is None:
        return

    window.font.default_width = new_value
    window.schedule_autosave()


def handle_default_spacing_edit(window: MainWindow, new_value: int):
    if window.font is None:
        return

    window.font.default_spacing = new_value
    window.schedule_autosave()


def handle_glyph_width_edit(window: MainWindow, new_value: int):
    if window.current_glyph is None:
        return

    window.current_glyph.width = new_value
    window.ui.glyphCanvas.update()
    window.schedule_autosave()


def handle_glyph_name_edit(window: MainWindow, new_text: str):
    font = window.font
    current_glyph = window.current_glyph
    current_item = window.ui.glyphSelectorList.currentItem()
    new_text = new_text.strip()

    if font is None or current_glyph is None or current_item is None:
        return

    if current_glyph.name == new_text:
        return

    is_duplicate = any(
        glyph.name == new_text
        for glyph in font.glyphs
        if glyph is not current_glyph
    )

    if is_duplicate:
        show_error(
            window,
            "Duplicate glyph",
            f"The glyph name '{new_text}' is already in use",
        )
        window.ui.identiferCharBox.setText(current_glyph.name)
        return

    current_glyph.name = new_text
    window.ui.selectedGlyphTitle.setText(f"Selected glyph: {new_text}")
    current_item.setText(new_text)
    window.schedule_autosave()


def trigger_add_glyph(window: MainWindow):
    font = window.font
    if font is None:
        return

    dialog = QDialog(window)
    dialog.setWindowTitle("Add new glyph")
    main_layout = QVBoxLayout(dialog)

    character_layout = QHBoxLayout()
    character_layout.addWidget(QLabel("Char / Identifier"))
    character_input = QLineEdit()
    character_layout.addWidget(character_input)
    main_layout.addLayout(character_layout)

    width_layout = QHBoxLayout()
    width_layout.addWidget(QLabel("Width"))
    width_spin = QSpinBox()
    width_spin.setMinimum(1)
    width_spin.setValue(font.default_width)
    width_layout.addWidget(width_spin)
    main_layout.addLayout(width_layout)

    duplicate_bitmap_layout = QHBoxLayout()
    duplicate_bitmap_layout.addWidget(QLabel("Duplicate bitmap of"))
    duplicate_bitmap_input = QLineEdit()
    duplicate_bitmap_layout.addWidget(duplicate_bitmap_input)
    main_layout.addLayout(duplicate_bitmap_layout)

    buttons = QDialogButtonBox(
        QDialogButtonBox.StandardButton.Ok
        | QDialogButtonBox.StandardButton.Cancel
    )
    buttons.accepted.connect(dialog.accept)
    buttons.rejected.connect(dialog.reject)
    main_layout.addWidget(buttons)

    if dialog.exec() != QDialog.DialogCode.Accepted:
        return

    new_character = character_input.text().strip()
    glyph_to_copy = duplicate_bitmap_input.text().strip()
    new_width = width_spin.value()

    if any(glyph.name == new_character for glyph in font.glyphs):
        show_error(
            window,
            "Duplicate glyph",
            f"The glyph '{new_character}' already exists",
        )
        return

    glyph_to_copy_obj = None

    for glyph in font.glyphs:
        if glyph.name == glyph_to_copy:
            glyph_to_copy_obj = glyph

    if glyph_to_copy_obj == None and glyph_to_copy != "":
        show_error(
            window,
            "Unknow glyph to copy from",
            f"The glyph '{glyph_to_copy}' is not within the font {font.name}" 
        )

    new_glyph = Glyph(new_character, font.height, font)
    set_width = new_width
    if not glyph_to_copy == "":
        set_width = glyph_to_copy_obj.width
        new_glyph.grid = copy.deepcopy(glyph_to_copy_obj.grid)
    new_glyph.width = set_width

    register_font_glyphs_to_window(window, font)
    matching_items = window.ui.glyphSelectorList.findItems(
        new_character,
        Qt.MatchFlag.MatchExactly,
    )
    if matching_items:
        window.ui.glyphSelectorList.setCurrentItem(matching_items[0])
    selected_glyph(window, new_glyph)
    window.schedule_autosave()


def trigger_remove_current_glyph(window: MainWindow):
    font = window.font
    glyph = window.current_glyph

    if font is None or glyph is None:
        return

    font.glyphs.remove(glyph)
    window.undo_stack.clear()
    window.redo_stack.clear()
    register_font_glyphs_to_window(window, font)
    selected_glyph(window, None)
    window.schedule_autosave()


def trigger_remove_all_glyphs(window: MainWindow):
    if window.font is None:
        return

    window.font.glyphs.clear()
    window.undo_stack.clear()
    window.redo_stack.clear()
    register_font_glyphs_to_window(window, window.font)
    selected_glyph(window, None)
    window.schedule_autosave()


def apply_drawing_action(window: MainWindow, action_name: str):
    glyph = window.current_glyph
    if glyph is None:
        return

    window.remember_drawing_state()
    getattr(glyph, action_name)()
    window.ui.glyphCanvas.update()
    window.schedule_autosave()


def connect_signals(window: MainWindow):
    window.ui.glyphSelectorList.itemClicked.connect(
        lambda item: selected_glyph(
            window,
            get_glyph_from_name(window.font, item.text()),
        )
    )

    window.ui.fontNameBox.textEdited.connect(
        lambda text: handle_font_name_edit(window, text)
    )
    window.ui.fontHeightBox.valueChanged.connect(
        lambda value: handle_font_height_edit(window, value)
    )
    window.ui.fontDefaultWidthBox.valueChanged.connect(
        lambda value: handle_default_width_edit(window, value)
    )
    window.ui.fontDefaultSpacingBox.valueChanged.connect(
        lambda value: handle_default_spacing_edit(window, value)
    )
    window.ui.widthBox.valueChanged.connect(
        lambda value: handle_glyph_width_edit(window, value)
    )
    window.ui.identiferCharBox.editingFinished.connect(
        lambda: handle_glyph_name_edit(
            window,
            window.ui.identiferCharBox.text(),
        )
    )

    window.ui.actionInvert.triggered.connect(
        lambda: apply_drawing_action(window, "invert")
    )
    window.ui.actionClear.triggered.connect(
        lambda: apply_drawing_action(window, "clear")
    )
    window.ui.actionLeft.triggered.connect(
        lambda: apply_drawing_action(window, "shift_left")
    )
    window.ui.actionRight.triggered.connect(
        lambda: apply_drawing_action(window, "shift_right")
    )
    window.ui.actionUp.triggered.connect(
        lambda: apply_drawing_action(window, "shift_up")
    )
    window.ui.actionDown.triggered.connect(
        lambda: apply_drawing_action(window, "shift_down")
    )

    window.ui.actionSelected.triggered.connect(
        lambda: trigger_remove_current_glyph(window)
    )
    window.ui.actionAll.triggered.connect(
        lambda: trigger_remove_all_glyphs(window)
    )
    window.ui.actionAdd.triggered.connect(lambda: trigger_add_glyph(window))

    window.ui.actionSave.triggered.connect(lambda: trigger_save(window))
    window.ui.actionSave_to_new_file.triggered.connect(
        lambda: trigger_save_to_new_file(window)
    )
    window.ui.actionOpen.triggered.connect(lambda: trigger_open(window))

    window.ui.actionOpenPreview.triggered.connect(lambda: trigger_preview(window))

def trigger_preview(window: MainWindow) -> None:
    window.preview_window.show()
    
def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()

    window.setWindowTitle("New font")

    window.preview_window = QDialog(window)
    window.preview_ui = Ui_Dialog()
    window.preview_ui.setupUi(window.preview_window)

    window.preview_window.resize(800, 250)
    window.preview_window.setMinimumSize(500, 180)
    window.preview_window.setWindowTitle("Font preview")
    window.preview_ui.lineEdit.textEdited.connect(lambda new_text: window.preview_ui.graphicsView.set_text(new_text))

    print(type(window.preview_ui.graphicsView))
    print(window.preview_ui.graphicsView.size())
    window.font = initialise_new_font()
    window.refresh_font_controls()
    connect_signals(window)

    window.preview_ui.graphicsView.set_font(window.font)

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
