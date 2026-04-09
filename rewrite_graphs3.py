import json

with open("materials/exam_part_modified.json", "r") as f:
    data = json.load(f)

complex_q_ids = [26, 29, 30, 34, 35]

for item in data:
    if item["id"] in complex_q_ids:
        new_elements = []
        for el in item.get("graph", {}).get("elements", []):
            if el["type"] == "line":
                new_elements.append(el)
            elif el["type"] == "polygon":
                el["fill"] = "none" # Remove any fill for polygons
                new_elements.append(el)
            elif el["type"] == "point":
                new_elements.append(el)
            elif el["type"] == "label":
                # Ensure it's just a simple text label
                new_elements.append(el)

        # Manually add the base geometric lines for the arcs if missing,
        # since we removed the `arc` primitive itself. We will connect the points via straight lines
        # or rely on the polygon/lines we already preserved.

        item["graph"]["elements"] = new_elements

with open("materials/exam_part_modified.json", "w") as f:
    json.dump(data, f, indent=4)

import shutil
shutil.copy("materials/exam_part_modified.json", "materials/exam_part.json")
