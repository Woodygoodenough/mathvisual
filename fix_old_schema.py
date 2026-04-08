import json

with open('materials/exam_part.json', 'r') as f:
    data = json.load(f)

for q in data:
    graph = q.get('graph')
    if graph and not isinstance(graph.get('elements'), list):
        print(f"Fixing schema for Q{q['id']}")
        elements = []

        # Add points
        points_dict = graph.get('points', {})

        # Add lines
        for line in graph.get('lines', []):
            el = {'type': 'line', 'points': []}
            for pt_name in line.get('points', []):
                el['points'].append(points_dict[pt_name])
            if 'style' in line: el['style'] = line['style']
            elements.append(el)

        # Add labels
        for label in graph.get('labels', []):
            el = {'type': 'label', 'text': label['text'], 'point': points_dict[label['point']]}
            if 'position' in label:
                # Map old positions
                pos = label['position']
                if pos == 'N': el['labelPosition'] = 'top'
                elif pos == 'S': el['labelPosition'] = 'bottom'
                elif pos == 'E': el['labelPosition'] = 'right'
                elif pos == 'W': el['labelPosition'] = 'left'
                elif pos == 'NE': el['labelPosition'] = 'top-right'
                elif pos == 'NW': el['labelPosition'] = 'top-left'
                elif pos == 'SE': el['labelPosition'] = 'bottom-right'
                elif pos == 'SW': el['labelPosition'] = 'bottom-left'
            elements.append(el)

        # Add right angles
        for ra in graph.get('right_angles', []):
            el = {
                'type': 'right_angle',
                'point': points_dict[ra['p2']],
                'line1': [points_dict[ra['p2']], points_dict[ra['p1']]],
                'line2': [points_dict[ra['p2']], points_dict[ra['p3']]]
            }
            elements.append(el)

        # Add annotations
        for ann in graph.get('annotations', []):
            # Midpoint logic
            p1 = points_dict[ann['p1']]
            p2 = points_dict[ann['p2']]
            mid_x = (p1[0] + p2[0]) / 2
            mid_y = (p1[1] + p2[1]) / 2
            el = {
                'type': 'label',
                'text': ann['text'],
                'point': [mid_x, mid_y]
            }
            if 'position' in ann:
                pos = ann['position']
                if pos == 'N': el['labelPosition'] = 'top'
                elif pos == 'S': el['labelPosition'] = 'bottom'
                elif pos == 'E': el['labelPosition'] = 'right'
                elif pos == 'W': el['labelPosition'] = 'left'
                elif pos == 'NE': el['labelPosition'] = 'top-right'
                elif pos == 'NW': el['labelPosition'] = 'top-left'
                elif pos == 'SE': el['labelPosition'] = 'bottom-right'
                elif pos == 'SW': el['labelPosition'] = 'bottom-left'
            elements.append(el)

        q['graph'] = {'elements': elements}

# Fix white space and other minor things
import re
with open("app/page.tsx", "r") as f:
    page = f.read()

page = page.replace('className="text-lg leading-relaxed"', 'className="text-lg leading-relaxed whitespace-pre-wrap"')

with open("app/page.tsx", "w") as f:
    f.write(page)

# Fix startAngle / sector
with open("components/MathGraph.jsx", "r") as f:
    math_graph = f.read()

math_graph = math_graph.replace("el.startAngle", "(el.startAngle !== undefined ? el.startAngle : el.start_angle)")
math_graph = math_graph.replace("el.endAngle", "(el.endAngle !== undefined ? el.endAngle : el.end_angle)")

# Add sector fallback
sector_code = """
            if (el.type === 'sector' || el.type === 'shaded_region') {
                return (
                    <polygon
                        key={`sector-${idx}`}
                        points={el.points ? el.points.map(pt => `${pt[0]},${trY(pt[1])}`).join(" ") : ""}
                        fill={el.fill || '#e5e7eb'}
                        stroke="none"
                        vectorEffect="non-scaling-stroke"
                    />
                );
            }
"""
math_graph = math_graph.replace("if (el.type === 'polygon') {", sector_code + "\n            if (el.type === 'polygon') {")


with open("components/MathGraph.jsx", "w") as f:
    f.write(math_graph)


with open('materials/exam_part.json', 'w') as f:
    json.dump(data, f, indent=4)
