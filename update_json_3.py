import json

new_questions = [
  {
    "id": "25",
    "text": "If $a > 0$, which of the following cannot be true?\nI. $\\sqrt{3a} + \\sqrt{6a} = 9\\sqrt{a}$\nII. $\\sqrt{\\frac{9a}{4}} = \\frac{3\\sqrt{a}}{2}$\nIII. $\\sqrt{12a} \\times \\sqrt{3a} = 6a$",
    "choices": {
      "A": "I only",
      "B": "III only",
      "C": "I and III only",
      "D": "II and III only"
    },
    "answer": "A",
    "graph": None
  },
  {
    "id": "26",
    "text": "In the figure, $AOB$ is a sector with centre $O$. $AO = 8 \\text{ cm}$ and $AO \\perp OB$. Find the perimeter of the shaded region, correct to 2 decimal places.",
    "choices": {
      "A": "$12.57 \\text{ cm}$",
      "B": "$18.27 \\text{ cm}$",
      "C": "$23.88 \\text{ cm}$",
      "D": "$28.57 \\text{ cm}$"
    },
    "answer": "C",
    "graph": {
      "type": "geometry",
      "elements": [
        {
          "type": "sector",
          "center": [0, 0],
          "radius": 100,
          "start_angle": 0,
          "end_angle": 90,
          "fill": "none",
          "stroke": "black"
        },
        {
          "type": "polygon",
          "points": [[0, 0], [100, 0], [0, 100]],
          "fill": "none",
          "stroke": "black"
        },
        {
          "type": "right_angle",
          "vertex": [0, 0],
          "point1": [100, 0],
          "point2": [0, 100],
          "size": 10
        },
        {
          "type": "label",
          "point": [-10, -10],
          "text": "$O$"
        },
        {
          "type": "label",
          "point": [0, 115],
          "text": "$A$"
        },
        {
          "type": "label",
          "point": [115, 0],
          "text": "$B$"
        },
        {
          "type": "label",
          "point": [-25, 50],
          "text": "$8 \\text{ cm}$"
        },
        {
          "type": "shaded_region",
          "shape": "custom",
          "paths": [
            "M 100 0 A 100 100 0 0 0 0 100 L 100 0 Z"
          ],
          "fill": "pink",
          "stroke": "none"
        }
      ]
    }
  },
  {
    "id": "27",
    "text": "Consider a solid right circular cylinder of base diameter $1 \\text{ cm}$ and height $6 \\text{ cm}$. Find the total surface area of the cylinder in terms of $\\pi$.",
    "choices": {
      "A": "$6\\pi \\text{ cm}^2$",
      "B": "$6.5\\pi \\text{ cm}^2$",
      "C": "$12\\pi \\text{ cm}^2$",
      "D": "$14\\pi \\text{ cm}^2$"
    },
    "answer": "B",
    "graph": None
  },
  {
    "id": "28",
    "text": "In $\\triangle ABC$, $AB : BC : AC = 7 : 24 : 25$. Find $\\cos A : \\tan C$.",
    "choices": {
      "A": "$7 : 25$",
      "B": "$25 : 7$",
      "C": "$24 : 25$",
      "D": "$25 : 24$"
    },
    "answer": "C",
    "graph": None
  }
]

with open('materials/exam_part.json', 'r') as f:
    data = json.load(f)

for q in new_questions:
    data = [x for x in data if x['id'] != q['id']]
    data.append(q)

data.sort(key=lambda x: int(x['id']))

with open('materials/exam_part.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Added 25-28")
