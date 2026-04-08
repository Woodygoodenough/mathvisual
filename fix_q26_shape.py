import json

with open('materials/exam_part.json', 'r') as f:
    data = json.load(f)

for q in data:
    if q.get('id') == 26:
        # Instead of polygon AND arc, let's just make it cleanly represent the sector with a line for AB
        elements = [el for el in q['graph']['elements'] if el.get('type') not in ('polygon', 'arc')]

        # Add the sector shape (AOB) and the line AB
        elements.insert(0, {
            "type": "sector",
            "center": [0, 0],
            "radius": 100,
            "startAngle": 0,
            "endAngle": 90,
            "fill": "none",
            "stroke": "black"
        })
        elements.insert(1, {
            "type": "line",
            "points": [[100, 0], [0, 100]]
        })
        q['graph']['elements'] = elements

with open('materials/exam_part.json', 'w') as f:
    json.dump(data, f, indent=4)
