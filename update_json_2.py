import json

new_questions = [
  {
    "id": "35",
    "text": "In the figure, $OPQ$ and $ORS$ are sectors with centre $O$, where $OP = 24 \\text{ cm}$ and $OR = 42 \\text{ cm}$. The area of the shaded region $PQSR$ is $264\\pi \\text{ cm}^2$. Which of the following is/are true?\n\nI. The angle of sector $OPQ$ is $80^\\circ$.\nII. The area of sector $OPQ$ is $72\\pi \\text{ cm}^2$.\nIII. The perimeter of sector $ORS$ is $\\frac{56}{3}\\pi \\text{ cm}$.",
    "choices": {
      "A": "I only",
      "B": "II only",
      "C": "I and III only",
      "D": "II and III only"
    },
    "answer": "A",
    "graph": {
      "points": {
        "O": [21, 42],
        "P": [6, 18],
        "Q": [36, 18],
        "R": [0, 0],
        "S": [42, 0]
      },
      "lines": [
        {"points": ["O", "R"], "style": "solid"},
        {"points": ["O", "S"], "style": "solid"}
      ],
      "arcs": [
        {"p1": "P", "p2": "Q", "center": "O"},
        {"p1": "R", "p2": "S", "center": "O"}
      ],
      "shaded_regions": [
        {"points": ["P", "Q", "S", "R"], "type": "sector_difference", "center": "O"}
      ],
      "labels": [
        {"point": "O", "text": "O", "position": "S"},
        {"point": "P", "text": "P", "position": "SE"},
        {"point": "Q", "text": "Q", "position": "SW"},
        {"point": "R", "text": "R", "position": "NW"},
        {"point": "S", "text": "S", "position": "NE"}
      ],
      "output_path": "graph_35.svg"
    }
  },
  {
    "id": "36",
    "text": "In the figure, $PQRS$ is a trapezium with $\\angle PQR = \\angle QRS = 90^\\circ$. $T$ and $U$ are points on $QR$ such that $QT = TU = UR$. Which of the following must be true?\n\nI. $RT \\cos a = QU \\cos b$\nII. $PU \\sin a = ST \\sin b$\nIII. $RS \\tan a = PQ \\tan b$",
    "choices": {
      "A": "I only",
      "B": "II only",
      "C": "I and III only",
      "D": "II and III only"
    },
    "answer": "B",
    "graph": {
      "points": {
        "P": [0, 30],
        "Q": [0, 0],
        "T": [15, 0],
        "U": [30, 0],
        "R": [45, 0],
        "S": [45, 20]
      },
      "lines": [
        {"points": ["P", "Q"], "style": "solid"},
        {"points": ["Q", "R"], "style": "solid"},
        {"points": ["R", "S"], "style": "solid"},
        {"points": ["S", "P"], "style": "solid"},
        {"points": ["P", "U"], "style": "solid"},
        {"points": ["S", "T"], "style": "solid"}
      ],
      "labels": [
        {"point": "P", "text": "P", "position": "NW"},
        {"point": "Q", "text": "Q", "position": "SW"},
        {"point": "T", "text": "T", "position": "S"},
        {"point": "U", "text": "U", "position": "S"},
        {"point": "R", "text": "R", "position": "SE"},
        {"point": "S", "text": "S", "position": "NE"}
      ],
      "angles": [
        {"p1": "Q", "p2": "P", "p3": "U", "text": "a"},
        {"p1": "R", "p2": "S", "p3": "T", "text": "b"}
      ],
      "right_angles": [
        {"p1": "P", "p2": "Q", "p3": "R", "size": 1.0},
        {"p1": "Q", "p2": "R", "p3": "S", "size": 1.0}
      ],
      "tick_marks": [
        {"p1": "Q", "p2": "T", "count": 1},
        {"p1": "T", "p2": "U", "count": 1},
        {"p1": "U", "p2": "R", "count": 1}
      ],
      "output_path": "graph_36.svg"
    }
  },
  {
    "id": "37",
    "text": "In the figure, $AD =$",
    "choices": {
      "A": "$AB \\cos \\alpha + BC \\cos \\beta$.",
      "B": "$AB \\cos \\alpha + BC \\sin \\beta$.",
      "C": "$AB \\sin \\alpha + BC \\cos \\beta$.",
      "D": "$AB \\sin \\alpha + BC \\sin \\beta$."
    },
    "answer": "B",
    "graph": {
      "points": {
        "A": [0, 0],
        "B": [15, 25],
        "C": [45, 40],
        "D": [45, 0]
      },
      "lines": [
        {"points": ["A", "B"], "style": "solid"},
        {"points": ["B", "C"], "style": "solid"},
        {"points": ["C", "D"], "style": "solid"},
        {"points": ["D", "A"], "style": "solid"}
      ],
      "labels": [
        {"point": "A", "text": "A", "position": "SW"},
        {"point": "B", "text": "B", "position": "NW"},
        {"point": "C", "text": "C", "position": "NE"},
        {"point": "D", "text": "D", "position": "SE"}
      ],
      "angles": [
        {"p1": "B", "p2": "A", "p3": "D", "text": "\\alpha"},
        {"p1": "B", "p2": "C", "p3": "D", "text": "\\beta"}
      ],
      "right_angles": [
        {"p1": "A", "p2": "D", "p3": "C", "size": 1.0}
      ],
      "output_path": "graph_37.svg"
    }
  }
]

with open('materials/exam_part.json', 'r') as f:
    data = json.load(f)

existing_ids = {q['id'] for q in data}
for q in new_questions:
    if q['id'] not in existing_ids:
        data.append(q)

data.sort(key=lambda x: int(x['id']))

with open('materials/exam_part.json', 'w') as f:
    json.dump(data, f, indent=2)
