from pathlib import Path

OUTPUT = Path("assets/info_card.svg")

svg = """<svg xmlns="http://www.w3.org/2000/svg" width="420" height="220">
<rect width="100%" height="100%" fill="#0d1117"/>

<style>
text{
font-family:monospace;
font-size:16px;
fill:#c9d1d9;
}
.green{fill:#3fb950;}
.blue{fill:#58a6ff;}
</style>

<text x="20" y="35" class="green">deepanshu@github</text>
<text x="20" y="60">---------------------------</text>

<text x="20" y="90"><tspan class="blue">OS:</tspan> Fedora Linux</text>
<text x="20" y="115"><tspan class="blue">Editor:</tspan> VS Code</text>
<text x="20" y="140"><tspan class="blue">Languages:</tspan> Python, JS</text>
<text x="20" y="165"><tspan class="blue">Focus:</tspan> AI • Full Stack</text>
<text x="20" y="190"><tspan class="blue">GitHub:</tspan> Deepanshu-Monocoder</text>

</svg>
"""

OUTPUT.write_text(svg)

print("Info card created!")