import re

with open("components/MathGraph.jsx", "r") as f:
    content = f.read()

search = """            if (el.type === 'right_angle') {
                const p2 = el.point; // Vertex
                const p1 = el.line1[1]; // Other point on line 1
                const p3 = el.line2[1]; // Other point on line 2
                const size = el.size || 1.5;"""

replace = """            if (el.type === 'right_angle') {
                const p2 = el.point || el.vertex; // Vertex
                let p1, p3;
                if (el.line1 && el.line2) {
                    p1 = el.line1[1];
                    p3 = el.line2[1];
                } else if (el.point1 && el.point2) {
                    p1 = el.point1;
                    p3 = el.point2;
                }
                const size = el.size || 1.5;"""

content = content.replace(search, replace)

with open("components/MathGraph.jsx", "w") as f:
    f.write(content)
