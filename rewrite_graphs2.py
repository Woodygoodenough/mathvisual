import json

with open("materials/exam_part_modified.json", "r") as f:
    data = json.load(f)

# Rewrite texts to be semantically equivalent but use point annotations instead of shading/sectors
for item in data:
    if item["id"] == 26:
        item["text"] = "In the figure, points $A$, $O$, and $B$ form a sector of a circle with center $O$. The radius $AO = 8 \\text{ cm}$ and $AO \\perp OB$. Let $C$ be the midpoint of the arc $AB$ (not shown) such that a segment connects $A$ to $B$. Find the perimeter of the region bounded by the line segment $AB$ and the arc $AB$, correct to 2 decimal places."
    elif item["id"] == 29:
        item["text"] = "In the figure, $D$ and $E$ are points on $BC$. It is given that $\\angle ADE = \\angle AED = 70^\\circ$, $\\angle BAE = 60^\\circ$, $AD = AE$, and $BE = DC$. Which of the following is/are true?\nI. $CE = BD$\nII. $\\angle CAD = 70^\\circ$\nIII. $\\triangle ACD \\cong \\triangle ABE$"
    elif item["id"] == 30:
        item["text"] = "In the figure, $OA \\perp AB$ with $AB = 8 \\text{ cm}$. $OAC$ is a sector of a circle with center $O$. A line segment is drawn from $O$ to $B$, intersecting the arc $AC$ at point $C$. The distance from $C$ to the line segment $OA$ is $17 \\text{ cm}$. Find the area of the region bounded by the segment $AC$, segment $CB$, and the arc $AC$, correct to 3 significant figures."
    elif item["id"] == 34:
        item["text"] = "In the figure, $PQRS$ is a square. Points $P$, $U$, $T$ are collinear, and points $Q$, $R$, $T$ are collinear.\n\nIf $RT = 2.1 \\text{ cm}$ and $TU = 2.9 \\text{ cm}$, find the length of the line segment $PU$."
    elif item["id"] == 35:
        item["text"] = "In the figure, $O, P, Q$ form a sector with center $O$ and radius $OP = 24 \\text{ cm}$. $O, R, S$ form a larger sector with center $O$ and radius $OR = 42 \\text{ cm}$. Points $O, P, R$ are collinear, and points $O, Q, S$ are collinear. The area of the region bounded by the line segments $PR, QS$ and arcs $PQ, RS$ is $264\\pi \\text{ cm}^2$. Which of the following is/are true?\n\nI. $\\angle POQ = 80^\\circ$.\nII. The area of sector $OPQ$ is $72\\pi \\text{ cm}^2$.\nIII. The perimeter of sector $ORS$ is $\\frac{56}{3}\\pi \\text{ cm}$."

with open("materials/exam_part_modified.json", "w") as f:
    json.dump(data, f, indent=4)
