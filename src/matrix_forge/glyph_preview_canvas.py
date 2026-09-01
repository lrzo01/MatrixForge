from PySide6.QtCore import QRectF
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QWidget

from .lib import Font, Glyph

class FontPreviewCanvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.font: Font | None = None
        self.text = ""

        self.setMinimumSize(500, 150)

        self.on_colour = QColor("orange")
        self.off_colour = QColor("black")
        self.outline_colour = QColor("grey")

    def set_font(self, font: Font | None) -> None:
        self.font = font
        self.update()

    def set_text(self, text: str) -> None:
        self.text = text
        print("Text Updated")
        self.update()

    def find_glyph(self, character: str) -> Glyph | None:
        if self.font is None:
            return None

        for glyph in self.font.glyphs:
            if glyph.name == character:
                return glyph

        return None

    def text_width(self) -> int:
        if self.font is None or not self.text:
            return 0

        width = 0

        for index, character in enumerate(self.text):
            glyph = self.find_glyph(character)

            if glyph is not None:
                width += glyph.width
            else:
                width += self.font.default_width

            if index < len(self.text) - 1:
                width += self.font.default_spacing

        return width

    def paintEvent(self, event) -> None:
        if self.font is None or not self.text:
            return

        matrix_width = self.text_width()
        matrix_height = self.font.height

        if matrix_width <= 0 or matrix_height <= 0:
            return

        cell_size = min(
            self.width() / matrix_width,
            self.height() / matrix_height,
        )

        rendered_width = matrix_width * cell_size
        rendered_height = matrix_height * cell_size

        origin_x = (self.width() - rendered_width) / 2
        origin_y = (self.height() - rendered_height) / 2

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(QPen(self.outline_colour, 1))

        cursor_x = origin_x

        for character in self.text:
            glyph = self.find_glyph(character)

            if glyph is None:
                cursor_x += (
                    self.font.default_width + self.font.default_spacing
                ) * cell_size
                continue

            self.paint_glyph(
                painter,
                glyph,
                cursor_x,
                origin_y,
                cell_size,
            )

            cursor_x += (
                glyph.width + self.font.default_spacing
            ) * cell_size

    def paint_glyph(
        self,
        painter: QPainter,
        glyph: Glyph,
        origin_x: float,
        origin_y: float,
        cell_size: float,
    ) -> None:
        dot_size = cell_size * 0.85
        dot_offset = (cell_size - dot_size) / 2

        for y in range(glyph.font.height):
            for x in range(glyph.width):
                dot_x = origin_x + x * cell_size + dot_offset
                dot_y = origin_y + y * cell_size + dot_offset

                state = glyph.read(x, y)

                if state:
                    painter.setBrush(self.on_colour)
                    painter.drawEllipse(
                        QRectF(dot_x, dot_y, dot_size, dot_size)
                    )