import json

new_questions = [
  {
    "id": "29",
    "text": "In the figure, $D$ and $E$ are points on $BC$. $\\angle ADE = \\angle AED = 70^\\circ$ and $\\angle BAE = 60^\\circ$, $AD = AE$, $BE = DC$. Which of the following is/are true?\nI. $CE = BD$\nII. $\\angle CAD = 70^\\circ$\nIII. $\\triangle ACD \\cong \\triangle ABE$",
    "choices": {
      "A": "I and II only",
      "B": "I and III only",
      "C": "II and III only",
      "D": "I, II and III only"
    },
    "answer": "B",
    "graph": {
      "type": "geometry",
      "elements": [
        {
          "type": "polygon",
          "points": [[0, 100], [150, 100], [75, 0]],
          "fill": "none",
          "stroke": "black"
        },
        {
          "type": "line",
          "point1": [75, 0],
          "point2": [50, 100]
        },
        {
          "type": "line",
          "point1": [75, 0],
          "point2": [100, 100]
        },
        {
          "type": "label",
          "point": [75, -15],
          "text": "$A$"
        },
        {
          "type": "label",
          "point": [-15, 115],
          "text": "$B$"
        },
        {
          "type": "label",
          "point": [165, 115],
          "text": "$C$"
        },
        {
          "type": "label",
          "point": [50, 115],
          "text": "$D$"
        },
        {
          "type": "label",
          "point": [100, 115],
          "text": "$E$"
        }
      ]
    }
  },
  {
    "id": "30",
    "text": "In the figure, $OA \\perp AB$. $OAC$ is a sector with center $O$. Find the area of the shaded region, correct to 3 significant figures.",
    "choices": {
      "A": "$1.10 \\text{ cm}^2$",
      "B": "$3.29 \\text{ cm}^2$",
      "C": "$4.88 \\text{ cm}^2$",
      "D": "$10.6 \\text{ cm}^2$"
    },
    "answer": "D",
    "graph": {
      "type": "geometry",
      "elements": [
        {
          "type": "polygon",
          "points": [[0, 100], [150, 100], [150, 20]],
          "fill": "none",
          "stroke": "black"
        },
        {
          "type": "right_angle",
          "vertex": [150, 100],
          "point1": [0, 100],
          "point2": [150, 20],
          "size": 10
        },
        {
          "type": "label",
          "point": [-15, 115],
          "text": "$O$"
        },
        {
          "type": "label",
          "point": [165, 115],
          "text": "$A$"
        },
        {
          "type": "label",
          "point": [165, 5],
          "text": "$B$"
        },
        {
          "type": "label",
          "point": [115, 35],
          "text": "$C$"
        },
        {
          "type": "label",
          "point": [165, 60],
          "text": "$8 \\text{ cm}$"
        },
        {
          "type": "label",
          "point": [75, 45],
          "text": "$17 \\text{ cm}$"
        },
        {
          "type": "shaded_region",
          "shape": "custom",
          "paths": [
            "M 150 100 L 150 20 L 118 38 A 150 150 0 0 0 150 100 Z"
          ],
          "fill": "gray",
          "stroke": "none"
        },
        {
          "type": "arc",
          "center": [0, 100],
          "radius": 150,
          "start_angle": 0,
          "end_angle": -28,
          "fill": "none",
          "stroke": "black"
        }
      ]
    }
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

print("Added 29-30")
