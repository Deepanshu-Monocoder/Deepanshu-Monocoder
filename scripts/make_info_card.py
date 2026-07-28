from pathlib import Path
from datetime import date
from dateutil.relativedelta import relativedelta

OUTPUT = Path("assets/info_card.svg")

# ----------------------------------------------------
# Dynamic Uptime
# ----------------------------------------------------

birth = date(2006, 7, 23)
today = date.today()

age = relativedelta(today, birth)
uptime = f"{age.years}y {age.months}m {age.days}d"

# ----------------------------------------------------
# Theme
# ----------------------------------------------------

BACKGROUND = "#0d1117"
TEXT = "#c9d1d9"
GREEN = "#3fb950"
BLUE = "#58a6ff"

FONT_SIZE = 19
LINE_HEIGHT = 30

SVG_WIDTH = 680

# ----------------------------------------------------
# Data
# ----------------------------------------------------

rows = [
    ("OS", "Fedora Linux"),
    ("Uptime", uptime),
    ("Status", "alive"),
    ("College", "IIT Madras"),
    ("IDE", "VS Code • Neovim"),
    ("Stack", "Python • Java • JavaScript"),
    ("", "Vue • HTML • CSS • SQL"),
    ("Learning", "Machine Learning"),
    ("", "System Design"),
    ("GitHub", "@Deepanshu-Monocoder"),
    ("LinkedIn", "/in/deepanshu-"),
    ("", "kumar-monocoder"),
    ("X", "@Deepanshu_CODE"),
    ("Hashnode", "@Deepanshu-Kumar"),
]

# ----------------------------------------------------
# Build SVG
# ----------------------------------------------------

height = 105 + len(rows) * LINE_HEIGHT

svg = f"""<svg xmlns="http://www.w3.org/2000/svg"
width="{SVG_WIDTH}"
height="{height}">

<rect width="100%" height="100%" fill="{BACKGROUND}"/>

<style>
text {{
    font-family: monospace;
    font-size:{FONT_SIZE}px;
    fill:{TEXT};
}}

.username {{
    fill:{GREEN};
    font-weight:bold;
}}

.label {{
    fill:{BLUE};
    font-weight:bold;
}}
</style>

<text x="20" y="35" class="username">Deepanshu-Monocoder@github</text>
<text x="20" y="60">────────────────────────────────────────────────────────────────────</text>
"""

y = 82

for label, value in rows:

    if label == "":
        svg += f'<text x="250" y="{y}">{value}</text>\n'

    else:
        dots = "." * max(2, 22 - len(label))

        svg += (
            f'<text x="20" y="{y}">'
            f'<tspan class="label">{label}</tspan>'
            f'{dots} {value}'
            f'</text>\n'
        )

    y += LINE_HEIGHT

svg += "</svg>"

OUTPUT.write_text(svg, encoding="utf-8")

print("Info card created successfully!")