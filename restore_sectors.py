import json

with open("materials/exam_part.json", "r") as f:
    data = json.load(f)

# Re-apply text rewrites so they still only mention points semantically.
for item in data:
    if item["id"] == 26:
        item["text"] = "In the figure, points $A$, $O$, and $B$ form a sector of a circle with center $O$. The radius $AO = 8 \\text{ cm}$ and $\\angle AOB = 90^\\circ$. Find the perimeter of the region bounded by the line segment $AB$ and the arc $AB$, correct to 2 decimal places."
        # Keep the sector/arc, but drop the right angle drawing and shaded fill
        new_els = []
        for el in item.get("graph", {}).get("elements", []):
            if el["type"] == "right_angle" or el["type"] == "tick":
                continue
            if el["type"] == "label" and len(el["text"].replace('$', '').replace('\\', '').strip()) > 2:
                continue
            if el["type"] == "sector":
                el["fill"] = "none" # Just an outline
            new_els.append(el)
        item["graph"]["elements"] = new_els

    elif item["id"] == 29:
        item["text"] = "In the figure, $D$ and $E$ are points on $BC$. It is given that $\\angle ADE = \\angle AED = 70^\\circ$, $\\angle BAE = 60^\\circ$, $AD = AE$, and $BE = DC$. Which of the following is/are true?\nI. $CE = BD$\nII. $\\angle CAD = 70^\\circ$\nIII. $\\triangle ACD \\cong \\triangle ABE$"
        new_els = []
        for el in item.get("graph", {}).get("elements", []):
            if el["type"] == "label" and len(el["text"].replace('$', '').replace('\\', '').strip()) > 2:
                continue
            if el["type"] == "tick" or el["type"] == "right_angle":
                continue
            new_els.append(el)
        item["graph"]["elements"] = new_els

    elif item["id"] == 30:
        item["text"] = "In the figure, $\\angle OAB = 90^\\circ$ with $AB = 8 \\text{ cm}$. $OAC$ is a sector of a circle with center $O$. A line segment is drawn from $O$ to $B$, intersecting the arc $AC$ at point $C$. The perpendicular distance from $C$ to the line segment $OA$ is $17 \\text{ cm}$. Find the area of the region bounded by the segment $AC$, segment $CB$, and the arc $AC$, correct to 3 significant figures."
        new_els = []
        for el in item.get("graph", {}).get("elements", []):
            if el["type"] == "right_angle" or el["type"] == "tick":
                continue
            if el["type"] == "label" and len(el["text"].replace('$', '').replace('\\', '').strip()) > 2:
                continue
            if el["type"] == "sector" or el["type"] == "shaded_region":
                el["fill"] = "none"
            new_els.append(el)
        item["graph"]["elements"] = new_els

    elif item["id"] == 34:
        item["text"] = "In the figure, $PQRS$ is a square. Points $P$, $U$, $T$ are collinear, and points $Q$, $R$, $T$ are collinear.\n\nIf $RT = 2.1 \\text{ cm}$ and $TU = 2.9 \\text{ cm}$, find the length of the line segment $PU$."
        new_els = []
        for el in item.get("graph", {}).get("elements", []):
            if el["type"] == "right_angle" or el["type"] == "tick":
                continue
            if el["type"] == "label" and len(el["text"].replace('$', '').replace('\\', '').strip()) > 2:
                continue
            new_els.append(el)
        item["graph"]["elements"] = new_els

    elif item["id"] == 35:
        item["text"] = "In the figure, $O, P, Q$ form a sector with center $O$ and radius $OP = 24 \\text{ cm}$. $O, R, S$ form a larger sector with center $O$ and radius $OR = 42 \\text{ cm}$. Points $O, P, R$ are collinear, and points $O, Q, S$ are collinear. The area of the region bounded by the line segments $PR, QS$ and arcs $PQ, RS$ is $264\\pi \\text{ cm}^2$. Which of the following is/are true?\n\nI. $\\angle POQ = 80^\\circ$.\nII. The area of sector $OPQ$ is $72\\pi \\text{ cm}^2$.\nIII. The perimeter of sector $ORS$ is $\\frac{56}{3}\\pi \\text{ cm}$."
        new_els = []
        for el in item.get("graph", {}).get("elements", []):
            if el["type"] == "right_angle" or el["type"] == "tick":
                continue
            if el["type"] == "label" and len(el["text"].replace('$', '').replace('\\', '').strip()) > 2:
                continue
            if el["type"] == "sector":
                el["fill"] = "none"
            new_els.append(el)
        # Ensure sectors actually exist since we had to patch this earlier
        if not any(el.get("type") == "sector" for el in new_els):
             new_els.append({
                 "type": "sector",
                 "center": [21, 42],
                 "radius": 24,
                 "startAngle": 270,
                 "endAngle": 350,
                 "fill": "none"
             })
             new_els.append({
                 "type": "sector",
                 "center": [21, 42],
                 "radius": 42,
                 "startAngle": 270,
                 "endAngle": 350,
                 "fill": "none"
             })
        item["graph"]["elements"] = new_els

with open("materials/exam_part.json", "w") as f:
    json.dump(data, f, indent=4)
