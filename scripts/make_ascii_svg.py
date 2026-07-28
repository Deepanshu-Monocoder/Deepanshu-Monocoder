from pathlib import Path
from PIL import Image
import html

INPUT = Path("assets/source_prepped.png")
OUTPUT = Path("assets/avi-ascii.svg")

ASCII_RAMP = (
    " .'`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
)

WIDTH = 130

FONT_SIZE = 8
LINE_HEIGHT = 9
CHAR_WIDTH = 4.8

BACKGROUND = "#0d1117"
FOREGROUND = "#c9d1d9"


def image_to_ascii():
    img = Image.open(INPUT).convert("L")

    # Preserve aspect ratio
    w, h = img.size
    aspect = h / w
    height = int(WIDTH * aspect * 0.55)

    img = img.resize((WIDTH, height), Image.Resampling.LANCZOS)

    pixels = list(img.getdata())

    ascii_chars = []

    ramp_len = len(ASCII_RAMP) - 1

    for p in pixels:
        index = int((p / 255) * ramp_len)
        ascii_chars.append(ASCII_RAMP[index])

    lines = []

    for i in range(0, len(ascii_chars), WIDTH):
        lines.append("".join(ascii_chars[i:i + WIDTH]))

    return lines


def build_svg(lines):
    width = max(len(line) for line in lines) * CHAR_WIDTH
    height = len(lines) * LINE_HEIGHT

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">

<rect width="100%" height="100%" fill="{BACKGROUND}"/>

<g
font-family="monospace"
font-size="{FONT_SIZE}"
fill="{FOREGROUND}"
xml:space="preserve">
'''

    for i, line in enumerate(lines):
        y = (i + 1) * LINE_HEIGHT
        svg += f'<text x="0" y="{y}">{html.escape(line)}</text>\n'

    svg += "</g></svg>"

    OUTPUT.write_text(svg)


if __name__ == "__main__":
    lines = image_to_ascii()
    build_svg(lines)
    print("SVG created successfully!")