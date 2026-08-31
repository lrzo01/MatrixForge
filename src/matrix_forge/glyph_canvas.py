from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import QRectF, Qt
from .lib import Glyph

class GlyphCanvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.glyph : None | Glyph = None
        self.drawing = True
        self.draw_value = 1
        self.cell_length = 1

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.draw_value = 1
            self.drawing = True
            self.draw_at_mouse(event)

        elif event.button() == Qt.MouseButton.RightButton:
            self.draw_value = 0
            self.drawing = True
            self.draw_at_mouse(event)

    def mouseMoveEvent(self, event):
        if self.drawing:
            self.draw_at_mouse(event)

    def mouseReleaseEvent(self, event):
        self.drawing = False

    def draw_at_mouse(self, event):
        if self.glyph is None:
            return
        
        x = int(event.position().x() / self.cell_length)
        y = int(event.position().y() / self.cell_length)

        self.glyph.write(x, y, self.draw_value)
        self.update()

    def paintEvent(self, event):
        if self.glyph is not None:
            x_length = float(self.glyph.width)
            y_length = float(self.glyph.font.height)

            x_abs_length = self.width()
            y_abs_length = self.height()

            cell_width = x_abs_length / x_length
            cell_height = y_abs_length / y_length

            self.cell_length = min(cell_width, cell_height)

            painter = QPainter(self)

            for y in range(int(y_length)):
                for x in range(int(x_length)):
                    cell_x = x * self.cell_length
                    cell_y = y * self.cell_length

                    dot_size = self.cell_length * 0.95

                    dot_x = cell_x + (self.cell_length - dot_size) / 2
                    dot_y = cell_y + (self.cell_length - dot_size) / 2

                    state = self.glyph.read(x, y)
                    painter.setPen(QPen(QColor("grey"), 1))

                    if state == True:
                        painter.setBrush(QColor("orange"))
                    else:
                        painter.setBrush(QColor("black"))

                    painter.drawEllipse(QRectF(dot_x, dot_y, dot_size, dot_size))