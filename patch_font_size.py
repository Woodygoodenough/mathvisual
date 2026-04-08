import re

with open("components/MathGraph.jsx", "r") as f:
    content = f.read()

# The labels in the screenshot look way too tiny. We need a default font size relative to the viewBox
search = """                        fontSize={el.fontSize || 1.2}"""
replace = """                        fontSize={el.fontSize || Math.max(1, width / 25)}"""

content = content.replace(search, replace)

with open("components/MathGraph.jsx", "w") as f:
    f.write(content)
