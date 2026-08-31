import typing

if typing.TYPE_CHECKING:
    from .glyph import Glyph
# to prevent circular dependency!

class Font:
    def __init__(self, name: str, height: int, default_spacing=1, default_width=8):
        self.name = name
        self._height = height  # Track internally
        self.default_spacing = default_spacing
        self.default_width = default_width
        self.glyphs: list['Glyph'] = []

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, new_height: int):
        if new_height == self._height or new_height < 1:
            return

        for glyph in self.glyphs:
            if new_height > self._height:
                for _ in range(new_height - self._height):
                    glyph.grid.append([0] * glyph.width)
            else:
                glyph.grid = glyph.grid[:new_height]

        self._height = new_height
