import json

new_questions = [
    {
        "id": 38,
        "text": "Consider two cylinders $P$ and $Q$ having the same height. If the ratio of the volume of $P$ to the volume of $Q$ is $1 : 4$, find base radius of cylinder $P$ : base radius of cylinder $Q$.",
        "choices": [
            "$2 : 1$",
            "$1 : 2$",
            "$16 : 1$",
            "$1 : 16$"
        ],
        "answer": "B"
    },
    {
        "id": 39,
        "text": "The figure shown below is formed by cutting away a semi-circle from two semi-circles of different sizes. Find the area of the figure, correct to 2 decimal places.",
        "choices": [
            "$6.28\\text{ m}^2$",
            "$7.85\\text{ m}^2$",
            "$9.42\\text{ m}^2$",
            "$12.57\\text{ m}^2$"
        ],
        "answer": "A",
        "graph": {
            "elements": [
                {
                    "type": "path",
                    "d": "M -2 0 A 2 2 0 0 1 2 0 A 1 1 0 0 0 0 0 L -2 0 Z",
                    "fill": "#ffe599",
                    "stroke": "none"
                },
                {
                    "type": "line",
                    "points": [[-2, 0], [2, 0]],
                    "style": "dashed"
                },
                {
                    "type": "arc",
                    "center": [0, 0],
                    "radius": 2,
                    "startAngle": 0,
                    "endAngle": 180
                },
                {
                    "type": "arc",
                    "center": [1, 0],
                    "radius": 1,
                    "startAngle": 0,
                    "endAngle": 180,
                    "style": "dashed"
                },
                {
                    "type": "line",
                    "points": [[-2, -0.2], [-2, -0.6]]
                },
                {
                    "type": "line",
                    "points": [[0, -0.2], [0, -0.6]]
                },
                {
                    "type": "line",
                    "points": [[2, -0.2], [2, -0.6]]
                },
                {
                    "type": "line",
                    "points": [[-2, -0.4], [0, -0.4]],
                    "arrows": "both"
                },
                {
                    "type": "line",
                    "points": [[0, -0.4], [2, -0.4]],
                    "arrows": "both"
                },
                {
                    "type": "label",
                    "point": [-1, -0.8],
                    "text": "$2\\text{ m}$"
                },
                {
                    "type": "label",
                    "point": [1, -0.8],
                    "text": "$2\\text{ m}$"
                }
            ]
        }
    },
    {
        "id": 40,
        "text": "In the figure, $ABCD$ is a rectangle. If $E$ is a point lying on $CD$ such that $\\angle CBE = 25^\\circ$, find $\\angle DAE$ correct to 2 decimal places.",
        "choices": [
            "$42.87^\\circ$",
            "$44.05^\\circ$",
            "$45.95^\\circ$",
            "$47.13^\\circ$"
        ],
        "answer": "C",
        "graph": {
            "elements": [
                {
                    "type": "polygon",
                    "points": [[0, 6], [0, 0], [4, 0], [4, 6]]
                },
                {
                    "type": "line",
                    "points": [[0, 6], [4, 1.865]]
                },
                {
                    "type": "line",
                    "points": [[0, 0], [4, 1.865]]
                },
                {
                    "type": "label",
                    "point": [-0.5, 6],
                    "text": "$A$"
                },
                {
                    "type": "label",
                    "point": [-0.5, 0],
                    "text": "$B$"
                },
                {
                    "type": "label",
                    "point": [4.5, 0],
                    "text": "$C$"
                },
                {
                    "type": "label",
                    "point": [4.5, 6],
                    "text": "$D$"
                },
                {
                    "type": "label",
                    "point": [4.5, 1.865],
                    "text": "$E$"
                },
                {
                    "type": "label",
                    "point": [-0.8, 3],
                    "text": "$6\\text{ cm}$"
                },
                {
                    "type": "label",
                    "point": [2, -0.8],
                    "text": "$4\\text{ cm}$"
                },
                {
                    "type": "arc",
                    "center": [0, 0],
                    "radius": 1.2,
                    "startAngle": 0,
                    "endAngle": 25
                },
                {
                    "type": "label",
                    "point": [1.6, 0.4],
                    "text": "$25^\\circ$"
                },
                {
                    "type": "arc",
                    "center": [0, 6],
                    "radius": 1.2,
                    "startAngle": -46,
                    "endAngle": 0
                },
                {
                    "type": "right_angle",
                    "point": [0, 0],
                    "line1": [[0, 0], [4, 0]],
                    "line2": [[0, 0], [0, 6]]
                },
                {
                    "type": "right_angle",
                    "point": [4, 0],
                    "line1": [[4, 0], [0, 0]],
                    "line2": [[4, 0], [4, 6]]
                },
                {
                    "type": "right_angle",
                    "point": [4, 6],
                    "line1": [[4, 6], [0, 6]],
                    "line2": [[4, 6], [4, 0]]
                },
                {
                    "type": "right_angle",
                    "point": [0, 6],
                    "line1": [[0, 6], [4, 6]],
                    "line2": [[0, 6], [0, 0]]
                }
            ]
        }
    }
]

with open('materials/exam_part.json', 'r') as f:
    data = json.load(f)

for item in data:
    try:
        item['id'] = int(item['id'])
    except ValueError:
        pass

data = [q for q in data if q['id'] not in [38, 39, 40]]
data.extend(new_questions)
data.sort(key=lambda x: int(x['id']) if isinstance(x['id'], (int, str)) and str(x['id']).isdigit() else x['id'])

with open('materials/exam_part.json', 'w') as f:
    json.dump(data, f, indent=4)
print("Added 38, 39, 40.")
