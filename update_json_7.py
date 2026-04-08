import json

new_questions = [
    {
        "id": 17,
        "text": "The figure shows the graph of the equation $4y - 3x - 50 = 0$. $P$ is a point lying on the graph. Find the $x$-coordinate of $P$.",
        "choices": [
            "$-16$",
            "$-12$",
            "$-8$",
            "$-6$"
        ],
        "answer": "D",
        "graph": {
            "elements": [
                {
                    "type": "line",
                    "points": [[-20, 0], [10, 0]],
                    "arrows": "end"
                },
                {
                    "type": "line",
                    "points": [[0, -5], [0, 20]],
                    "arrows": "end"
                },
                {
                    "type": "label",
                    "point": [9, -2],
                    "text": "$x$"
                },
                {
                    "type": "label",
                    "point": [-2, 19],
                    "text": "$y$"
                },
                {
                    "type": "line",
                    "points": [[-20, -2.5], [10, 20]],
                    "arrows": "both"
                },
                {
                    "type": "label",
                    "point": [-6, 17],
                    "text": "$4y - 3x - 50 = 0$"
                },
                {
                    "type": "point",
                    "point": [-6, 8],
                    "label": "$P$",
                    "labelPosition": "top-left"
                },
                {
                    "type": "line",
                    "points": [[-6, 8], [5, 8]],
                    "style": "dashed"
                },
                {
                    "type": "line",
                    "points": [[5, 8], [5, 0]],
                    "style": "dashed"
                },
                {
                    "type": "right_angle",
                    "point": [5, 0],
                    "line1": [[5, 0], [5, 8]],
                    "line2": [[5, 0], [0, 0]]
                },
                {
                    "type": "label",
                    "point": [6.5, 4],
                    "text": "$8$"
                }
            ]
        }
    },
    {
        "id": 18,
        "text": "In a class, there are $39$ students and the number of boys is $15$ more than that of girls. What is the ratio of the number of boys to that of girls in this class?",
        "choices": [
            "$9 : 4$",
            "$8 : 5$",
            "$5 : 8$",
            "$4 : 9$"
        ],
        "answer": "A"
    },
    {
        "id": 19,
        "text": "Which of the following are the possible lengths of the sides of a right-angled triangle?\nI. $11\\text{ cm}$, $13\\text{ cm}$, $17\\text{ cm}$\nII. $2.4\\text{ cm}$, $7\\text{ cm}$, $7.4\\text{ cm}$\nIII. $\\sqrt{5}\\text{ cm}$, $2\\text{ cm}$, $3\\text{ cm}$",
        "choices": [
            "I and II only",
            "I and III only",
            "II and III only",
            "I, II and III"
        ],
        "answer": "C"
    }
]

with open('materials/exam_part.json', 'r') as f:
    data = json.load(f)

# Ensure ID is int where possible
for item in data:
    try:
        item['id'] = int(item['id'])
    except ValueError:
        pass

# Remove existing Q17-Q19 to avoid duplication
data = [q for q in data if q['id'] not in [17, 18, 19]]

# Append and sort
data.extend(new_questions)
data.sort(key=lambda x: int(x['id']) if isinstance(x['id'], (int, str)) and str(x['id']).isdigit() else x['id'])

with open('materials/exam_part.json', 'w') as f:
    json.dump(data, f, indent=4)
print("Added 17, 18, 19.")
