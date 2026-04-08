import json
with open('materials/exam_part.json', 'r') as f:
    data = json.load(f)
ids = [int(q['id']) for q in data]
missing = [i for i in range(1, 41) if i not in ids]
print("Missing IDs:", missing)
print("Total Questions:", len(ids))
