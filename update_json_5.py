import json

new_questions = [
  {
    "id": "13",
    "text": "Which of the following triangles must be similar to $\\triangle ABC$ as shown above?",
    "choices": {
      "A": "A",
      "B": "B",
      "C": "C",
      "D": "D"
    },
    "answer": "D",
    "graph": {
      "type": "geometry",
      "elements": [
        { "type": "polygon", "points": [[50, 50], [100, 0], [150, 50]], "fill": "none", "stroke": "black" },
        { "type": "label", "point": [35, 50], "text": "$A$" },
        { "type": "label", "point": [160, 50], "text": "$B$" },
        { "type": "label", "point": [100, -10], "text": "$C$" },
        { "type": "label", "point": [75, 20], "text": "$2$" },
        { "type": "label", "point": [100, 60], "text": "$3$" },
        { "type": "label", "point": [65, 45], "text": "$30^\\circ$" },

        { "type": "label", "point": [0, 100], "text": "A." },
        { "type": "polygon", "points": [[20, 150], [70, 100], [120, 150]], "fill": "none", "stroke": "black" },
        { "type": "label", "point": [35, 145], "text": "$30^\\circ$" },
        { "type": "label", "point": [70, 165], "text": "$5$" },
        { "type": "label", "point": [100, 120], "text": "$4$" },

        { "type": "label", "point": [150, 100], "text": "B." },
        { "type": "polygon", "points": [[170, 150], [220, 100], [270, 150]], "fill": "none", "stroke": "black" },
        { "type": "label", "point": [255, 145], "text": "$30^\\circ$" },
        { "type": "label", "point": [220, 165], "text": "$6$" },
        { "type": "label", "point": [190, 120], "text": "$4$" },

        { "type": "label", "point": [0, 200], "text": "C." },
        { "type": "polygon", "points": [[20, 250], [70, 200], [120, 250]], "fill": "none", "stroke": "black" },
        { "type": "label", "point": [35, 245], "text": "$30^\\circ$" },
        { "type": "label", "point": [40, 220], "text": "$4$" },
        { "type": "label", "point": [100, 220], "text": "$6$" },

        { "type": "label", "point": [150, 200], "text": "D." },
        { "type": "polygon", "points": [[170, 250], [220, 200], [270, 250]], "fill": "none", "stroke": "black" },
        { "type": "label", "point": [255, 245], "text": "$30^\\circ$" },
        { "type": "label", "point": [220, 265], "text": "$6$" },
        { "type": "label", "point": [250, 220], "text": "$4$" }
      ]
    }
  },
  {
    "id": "14",
    "text": "In the figure, $BCD$ is a straight line and $\\angle BAC = \\angle ADC$. Which of the following must be correct?",
    "choices": {
      "A": "$\\triangle ABC \\sim \\triangle ACD$",
      "B": "$\\triangle ACD \\sim \\triangle ABD$",
      "C": "$\\triangle ABC \\sim \\triangle DBA$",
      "D": "$\\triangle ACD \\sim \\triangle CBA$"
    },
    "answer": "C",
    "graph": {
      "type": "geometry",
      "elements": [
        { "type": "polygon", "points": [[100, 0], [0, 100], [250, 100]], "fill": "none", "stroke": "black" },
        { "type": "line", "point1": [100, 0], "point2": [80, 100] },
        { "type": "label", "point": [100, -15], "text": "$A$" },
        { "type": "label", "point": [-15, 105], "text": "$B$" },
        { "type": "label", "point": [80, 115], "text": "$C$" },
        { "type": "label", "point": [265, 105], "text": "$D$" }
      ]
    }
  },
  {
    "id": "15",
    "text": "Which of the following points lies on the graph of $3x - 2y + 5 = 0$?",
    "choices": {
      "A": "$(-3, 4)$",
      "B": "$(-1, 2)$",
      "C": "$(1, 5)$",
      "D": "$(5, 10)$"
    },
    "answer": "D",
    "graph": None
  },
  {
    "id": "16",
    "text": "If $\\begin{cases} 4x - 5y = 22 \\\\ 3x + y = 26 \\end{cases}$, then $x + y =$",
    "choices": {
      "A": "10.",
      "B": "6.",
      "C": "-6.",
      "D": "-10."
    },
    "answer": "A",
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

print("Added 13-16")
