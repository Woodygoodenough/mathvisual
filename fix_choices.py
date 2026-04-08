import json

with open('materials/exam_part.json', 'r') as f:
    data = json.load(f)

letters = ["A", "B", "C", "D"]

for q in data:
    if isinstance(q.get("choices"), list):
        new_choices = {}
        for i, choice in enumerate(q["choices"]):
            if i < len(letters):
                new_choices[letters[i]] = choice
        q["choices"] = new_choices

with open('materials/exam_part.json', 'w') as f:
    json.dump(data, f, indent=4)
