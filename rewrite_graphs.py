import json

with open("materials/exam_part.json", "r") as f:
    data = json.load(f)

complex_q_ids = [26, 29, 30, 34, 35]

for item in data:
    if item["id"] in complex_q_ids:
        print(f"\n--- Question {item['id']} ---")
        print("Original Text:", item["text"])

        # We will keep only points, lines, polygons, and point labels
        new_elements = []
        for el in item.get("graph", {}).get("elements", []):
            if el["type"] in ["line", "polygon", "point"]:
                new_elements.append(el)
            elif el["type"] == "label":
                # Only keep alphabetical labels representing points, strip others
                if len(el["text"].replace('$', '').replace('\\', '').strip()) <= 2:
                    new_elements.append(el)

        item["graph"]["elements"] = new_elements

with open("materials/exam_part_modified.json", "w") as f:
    json.dump(data, f, indent=4)
