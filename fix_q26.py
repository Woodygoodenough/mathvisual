import json

with open('materials/exam_part.json', 'r') as f:
    data = json.load(f)

for q in data:
    if q.get('id') == 26:
        # Re-verify and explicitly modify it
        elements = q['graph']['elements']
        has_arc = any(el.get('type') == 'arc' for el in elements)
        if not has_arc:
            elements.insert(1, {
                "type": "arc",
                "center": [0, 0],
                "radius": 100,
                "startAngle": 0,
                "endAngle": 90,
                "style": "solid",
                "stroke": "black"
            })

with open('materials/exam_part.json', 'w') as f:
    json.dump(data, f, indent=4)
