import json

with open("materials/exam_part.json", "r") as f:
    data = json.load(f)

for item in data:
    if item["id"] == 35:
        item["graph"]["elements"].append({
            "type": "sector",
            "center": [21, 42],
            "radius": 24,
            "startAngle": 270,
            "endAngle": 350,
            "fill": "#d1d5db"
        })
        item["graph"]["elements"].append({
            "type": "sector",
            "center": [21, 42],
            "radius": 42,
            "startAngle": 270,
            "endAngle": 350,
            "fill": "#9ca3af"
        })

with open("materials/exam_part.json", "w") as f:
    json.dump(data, f, indent=4)
