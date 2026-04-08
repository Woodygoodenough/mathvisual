import re

with open("components/MathGraph.jsx", "r") as f:
    content = f.read()

search = """            if (el.type === 'line') {
                const pts = el.points.map(pt => `${pt[0]},${trY(pt[1])}`).join(" ");

                // Arrows (simple marker implementations could go here, but omitted for simplicity unless needed)
                return (
                    <polyline
                        key={`line-${idx}`}
                        points={pts}
                        fill="none"
                        stroke="black"
                        strokeWidth={0.5}
                        strokeDasharray={el.style === 'dashed' ? '2,2' : 'none'}
                        vectorEffect="non-scaling-stroke"
                    />
                );
            }"""

replace = """            if (el.type === 'line') {
                let pts = "";
                if (el.points) {
                    pts = el.points.map(pt => `${pt[0]},${trY(pt[1])}`).join(" ");
                } else if (el.point1 && el.point2) {
                    pts = `${el.point1[0]},${trY(el.point1[1])} ${el.point2[0]},${trY(el.point2[1])}`;
                }

                if (!pts) return null;

                // Arrows (simple marker implementations could go here, but omitted for simplicity unless needed)
                return (
                    <polyline
                        key={`line-${idx}`}
                        points={pts}
                        fill="none"
                        stroke="black"
                        strokeWidth={0.5}
                        strokeDasharray={el.style === 'dashed' ? '2,2' : 'none'}
                        vectorEffect="non-scaling-stroke"
                    />
                );
            }"""

content = content.replace(search, replace)

with open("components/MathGraph.jsx", "w") as f:
    f.write(content)
