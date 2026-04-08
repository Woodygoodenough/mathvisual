import json

new_questions = [
  {
    "id": "9",
    "text": "If $(x + y) : (3x + y) = 3 : 4$, then $x : y =$",
    "choices": {
      "A": "$5 : 1$.",
      "B": "$1 : 5$.",
      "C": "$2 : 7$.",
      "D": "$7 : 2$."
    },
    "answer": "B",
    "graph": None
  },
  {
    "id": "10",
    "text": "In the figure, the congruence of $\\triangle ABC$ and $\\triangle DEC$ can be expressed by both $\\triangle ABC \\cong \\triangle ADEC$ and $\\triangle ABC \\cong \\triangle ADCE$. Which of the following must be correct?\nI. $\\angle ABC = \\angle ACB$\nII. $DC = DE$\nIII. $BCD$ is a straight line.",
    "choices": {
      "A": "I only",
      "B": "II only",
      "C": "III only",
      "D": "I and II only"
    },
    "answer": "D",
    "graph": {
      "type": "geometry",
      "elements": [
        { "type": "polygon", "points": [[50, 0], [0, 80], [100, 80]], "fill": "none", "stroke": "black" },
        { "type": "polygon", "points": [[100, 80], [200, 80], [150, 160]], "fill": "none", "stroke": "black" },
        { "type": "label", "point": [50, -15], "text": "$A$" },
        { "type": "label", "point": [-15, 80], "text": "$B$" },
        { "type": "label", "point": [100, 100], "text": "$C$" },
        { "type": "label", "point": [215, 80], "text": "$D$" },
        { "type": "label", "point": [150, 175], "text": "$E$" },
        { "type": "tick", "point": [25, 40], "angle": 30, "style": "double" },
        { "type": "tick", "point": [125, 120], "angle": 30, "style": "double" },
        { "type": "tick", "point": [75, 40], "angle": -30, "style": "single" },
        { "type": "tick", "point": [175, 120], "angle": -30, "style": "single" },
        { "type": "tick", "point": [50, 80], "angle": 90, "style": "single_cross" },
        { "type": "tick", "point": [150, 80], "angle": 90, "style": "single_cross" }
      ]
    }
  },
  {
    "id": "11",
    "text": "It is given that 1 Euro can be exchanged for 10.8 Hong Kong dollars and 1 US dollar can be exchanged for 7.78 Hong Kong dollars. Thus 1 Euro can be exchanged for",
    "choices": {
      "A": "0.72 US dollars (cor. to 2 d.p.).",
      "B": "1.39 US dollars (cor. to 2 d.p.).",
      "C": "5.60 US dollars (cor. to 2 d.p.).",
      "D": "84.02 US dollars (cor. to 2 d.p.)."
    },
    "answer": "B",
    "graph": None
  },
  {
    "id": "12",
    "text": "If $\\triangle ABC \\sim \\triangle QPR$, where $AB = 7 \\text{ cm}$, $BC = 6 \\text{ cm}$, $CA = 4 \\text{ cm}$ and $PR = 3 \\text{ cm}$, then $QR =$",
    "choices": {
      "A": "$2 \\text{ cm}$.",
      "B": "$3 \\text{ cm}$.",
      "C": "$3.5 \\text{ cm}$.",
      "D": "$4 \\text{ cm}$."
    },
    "answer": "D",
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

print("Added 9-12")
