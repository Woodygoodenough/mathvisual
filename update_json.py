import json
import sys

new_questions = [
  {
    "id": "20",
    "text": "Two ships $A$ and $B$ leave port $P$ at noon. Ship $A$ sails due south of $P$ at a constant speed of $15 \\text{ km/h}$. Ship $B$ sails due west of $P$ at a constant speed of $20 \\text{ km/h}$. Find the distance between ships $A$ and $B$ at 3:30 pm that day.",
    "choices": {
      "A": "$25 \\text{ km}$",
      "B": "$55 \\text{ km}$",
      "C": "$87.5 \\text{ km}$",
      "D": "$122.5 \\text{ km}$"
    },
    "answer": "C",
    "graph": None
  },
  {
    "id": "21",
    "text": "Which of the following numbers is an irrational number?",
    "choices": {
      "A": "$2.5$",
      "B": "$1 \\frac{3}{7}$",
      "C": "$3.1\\dot{4}1\\dot{5}$",
      "D": "$\\sqrt{10}$"
    },
    "answer": "D",
    "graph": None
  },
  {
    "id": "22",
    "text": "If $\\sqrt{x} = 8$, then $\\sqrt{x - 15} =$",
    "choices": {
      "A": "$\\sqrt{7}$",
      "B": "$7$",
      "C": "$15$",
      "D": "$49$"
    },
    "answer": "B",
    "graph": None
  },
  {
    "id": "23",
    "text": "If $x > 0$, then $\\sqrt{36x} + \\sqrt{4x} =$",
    "choices": {
      "A": "$8\\sqrt{x}$",
      "B": "$\\sqrt{40x}$",
      "C": "$10\\sqrt{x}$",
      "D": "$20\\sqrt{x}$"
    },
    "answer": "A",
    "graph": None
  },
  {
    "id": "24",
    "text": "If $a, b > 0$, expand $(\\sqrt{27a} - \\sqrt{48b})^2$.",
    "choices": {
      "A": "$27a + 48b + 24\\sqrt{ab}$",
      "B": "$27a + 48b - 72\\sqrt{ab}$",
      "C": "$27a + 48b - 24\\sqrt{ab}$",
      "D": "$27a + 48b + 72\\sqrt{ab}$"
    },
    "answer": "B",
    "graph": None
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
