import re

with open("components/MathGraph.jsx", "r") as f:
    content = f.read()

search = """            if (el.type === 'tick') {
                const midX = (el.p1[0] + el.p2[0]) / 2;
                const midY = (el.p1[1] + el.p2[1]) / 2;

                const dx = el.p2[0] - el.p1[0];
                const dy = el.p2[1] - el.p1[1];
                const len = Math.sqrt(dx * dx + dy * dy);

                const nx = -dy / len;
                const ny = dx / len;

                const tickLen = 0.8;

                if (el.count === 1) {
                    return (
                        <line
                            key={`tick-${idx}`}
                            x1={midX - nx * tickLen} y1={trY(midY - ny * tickLen)}
                            x2={midX + nx * tickLen} y2={trY(midY + ny * tickLen)}
                            stroke="black" strokeWidth={0.5} vectorEffect="non-scaling-stroke"
                        />
                    );
                } else if (el.count === 2) {
                    const sepX = (dx / len) * 0.4;
                    const sepY = (dy / len) * 0.4;
                    return (
                        <g key={`tick-${idx}`}>
                            <line
                                x1={midX - sepX - nx * tickLen} y1={trY(midY - sepY - ny * tickLen)}
                                x2={midX - sepX + nx * tickLen} y2={trY(midY - sepY + ny * tickLen)}
                                stroke="black" strokeWidth={0.5} vectorEffect="non-scaling-stroke"
                            />
                            <line
                                x1={midX + sepX - nx * tickLen} y1={trY(midY + sepY - ny * tickLen)}
                                x2={midX + sepX + nx * tickLen} y2={trY(midY + sepY + ny * tickLen)}
                                stroke="black" strokeWidth={0.5} vectorEffect="non-scaling-stroke"
                            />
                        </g>
                    );
                }
            }"""

replace = """            if (el.type === 'tick') {
                if (el.p1 && el.p2) {
                    const midX = (el.p1[0] + el.p2[0]) / 2;
                    const midY = (el.p1[1] + el.p2[1]) / 2;

                    const dx = el.p2[0] - el.p1[0];
                    const dy = el.p2[1] - el.p1[1];
                    const len = Math.sqrt(dx * dx + dy * dy);

                    const nx = -dy / len;
                    const ny = dx / len;

                    const tickLen = 0.8;

                    if (el.count === 1) {
                        return (
                            <line
                                key={`tick-${idx}`}
                                x1={midX - nx * tickLen} y1={trY(midY - ny * tickLen)}
                                x2={midX + nx * tickLen} y2={trY(midY + ny * tickLen)}
                                stroke="black" strokeWidth={0.5} vectorEffect="non-scaling-stroke"
                            />
                        );
                    } else if (el.count === 2) {
                        const sepX = (dx / len) * 0.4;
                        const sepY = (dy / len) * 0.4;
                        return (
                            <g key={`tick-${idx}`}>
                                <line
                                    x1={midX - sepX - nx * tickLen} y1={trY(midY - sepY - ny * tickLen)}
                                    x2={midX - sepX + nx * tickLen} y2={trY(midY - sepY + ny * tickLen)}
                                    stroke="black" strokeWidth={0.5} vectorEffect="non-scaling-stroke"
                                />
                                <line
                                    x1={midX + sepX - nx * tickLen} y1={trY(midY + sepY - ny * tickLen)}
                                    x2={midX + sepX + nx * tickLen} y2={trY(midY + sepY + ny * tickLen)}
                                    stroke="black" strokeWidth={0.5} vectorEffect="non-scaling-stroke"
                                />
                            </g>
                        );
                    }
                } else if (el.point && el.angle !== undefined) {
                    const angleRad = el.angle * Math.PI / 180;
                    const tickLen = 3; // Make it visible

                    const dx = Math.cos(angleRad) * tickLen;
                    const dy = Math.sin(angleRad) * tickLen;

                    const midX = el.point[0];
                    const midY = el.point[1];

                    // If it has multiple ticks
                    if (el.count === 2) {
                        const sepDirRad = angleRad + Math.PI/2;
                        const sepX = Math.cos(sepDirRad) * 1.5;
                        const sepY = Math.sin(sepDirRad) * 1.5;

                        return (
                            <g key={`tick-${idx}`}>
                                <line
                                    x1={midX - sepX - dx} y1={trY(midY - sepY - dy)}
                                    x2={midX - sepX + dx} y2={trY(midY - sepY + dy)}
                                    stroke="black" strokeWidth={1} vectorEffect="non-scaling-stroke"
                                />
                                <line
                                    x1={midX + sepX - dx} y1={trY(midY + sepY - dy)}
                                    x2={midX + sepX + dx} y2={trY(midY + sepY + dy)}
                                    stroke="black" strokeWidth={1} vectorEffect="non-scaling-stroke"
                                />
                            </g>
                        );
                    }

                    return (
                        <line
                            key={`tick-${idx}`}
                            x1={midX - dx} y1={trY(midY - dy)}
                            x2={midX + dx} y2={trY(midY + dy)}
                            stroke="black" strokeWidth={1} vectorEffect="non-scaling-stroke"
                        />
                    );
                }
            }"""

content = content.replace(search, replace)

with open("components/MathGraph.jsx", "w") as f:
    f.write(content)
