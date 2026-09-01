from ..lib import Font, Glyph
import json

def font_to_json(font: Font) -> str:
    payload = {
        "name": font.name,
        "default_width": font.default_width,
        "spacing": font.default_spacing,
        "height": font.height,
        "markers": font.markers,
        "glyphs": {}
    }

    glyph: Glyph
    for glyph in font.glyphs:
        glyph_payload = {
            "identifier": glyph.name,
            "width": glyph.width,
            "bitmap": glyph.grid
        }

        payload["glyphs"][glyph_payload["identifier"]] = glyph_payload

    return json.dumps(payload)

def json_to_font(json_font: str) -> Font:
    decoded = json.loads(json_font)

    markers = decoded.get("markers")
    if markers is None:
        markers = []
     # migration compat from 0.1.2 to 0.1.3

    created_font = Font(decoded["name"], decoded["height"], decoded["spacing"], decoded["default_width"], markers)

    for glyph in decoded["glyphs"].values():
        created_glyph = Glyph(glyph["identifier"], glyph["width"], created_font)
        created_glyph.grid = glyph["bitmap"]

    return created_font




        
