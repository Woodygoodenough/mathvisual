import React from 'react';

// Direction vectors for native string parsing in offsets

const normalizeVector = (dx, dy) => {
  const len = Math.sqrt(dx * dx + dy * dy);
  if (len === 0) return [0, 0];
  return [dx / len, dy / len];
};

export default function MathGraph({ data }) {
  if (!data || !data.elements) {
      return null;
  }

  // To handle dynamic coordinates, we will dynamically calculate a viewBox.
  // The SVG viewBox will cover the min and max X, Y coordinates, plus some padding.
  let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;

  // Function to update bounding box
  const updateBounds = (x, y) => {
      if (x < minX) minX = x;
      if (x > maxX) maxX = x;
      if (y < minY) minY = y;
      if (y > maxY) maxY = y;
  };

  data.elements.forEach(el => {
      if (el.point) updateBounds(el.point[0], el.point[1]);
      if (el.points) {
          el.points.forEach(pt => updateBounds(pt[0], pt[1]));
      }
      if (el.center) {
          updateBounds(el.center[0] - (el.radius || 0), el.center[1] - (el.radius || 0));
          updateBounds(el.center[0] + (el.radius || 0), el.center[1] + (el.radius || 0));
      }
  });

  // Calculate bounding box width and height
  let width = maxX - minX;
  let height = maxY - minY;

  // Default dimensions if only one point
  if (width === 0) width = 10;
  if (height === 0) height = 10;

  // Add padding
  const paddingX = width * 0.15 || 5;
  const paddingY = height * 0.15 || 5;

  const viewBox = `${minX - paddingX} ${-maxY - paddingY} ${width + paddingX*2} ${height + paddingY*2}`;

  // Y is inverted visually in SVG (up is negative Y). We just negate the mathematical Y.
  const trY = (y) => -y;

  return (
    <div className="w-full max-w-[500px] border border-gray-200 bg-white p-4 shadow-sm my-4">
      <svg
        viewBox={viewBox}
        xmlns="http://www.w3.org/2000/svg"
        className="w-full h-auto"
        vectorEffect="non-scaling-stroke"
      >
        {data.elements.map((el, idx) => {
            if (el.type === 'line') {
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
            }

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

            if (el.type === 'polygon') {
                const pts = el.points.map(pt => `${pt[0]},${trY(pt[1])}`).join(" ");
                return (
                    <polygon
                        key={`poly-${idx}`}
                        points={pts}
                        fill={el.fill || 'none'}
                        stroke="black"
                        strokeWidth={0.5}
                        vectorEffect="non-scaling-stroke"
                    />
                );
            }
            if (el.type === 'path') {
                // If the path contains A (arc), we need to ensure Y coordinates are inverted in the data
                // For simplicity, we just use the raw path string and apply a generic SVG transform
                return (
                    <g key={`pathg-${idx}`} transform="scale(1, -1)">
                        <path
                            key={`path-${idx}`}
                            d={el.d}
                            fill={el.fill || 'none'}
                            stroke={el.stroke || 'black'}
                            strokeWidth={0.5}
                            vectorEffect="non-scaling-stroke"
                        />
                    </g>
                );
            }
            if (el.type === 'right_angle') {
                const p2 = el.point || el.vertex; // Vertex
                let p1, p3;
                if (el.line1 && el.line2) {
                    p1 = el.line1[1];
                    p3 = el.line2[1];
                } else if (el.point1 && el.point2) {
                    p1 = el.point1;
                    p3 = el.point2;
                }
                const size = el.size || 1.5;

                const v1 = normalizeVector(p1[0] - p2[0], p1[1] - p2[1]);
                const v2 = normalizeVector(p3[0] - p2[0], p3[1] - p2[1]);

                const pt1X = p2[0] + v1[0] * size;
                const pt1Y = p2[1] + v1[1] * size;
                const pt2X = p2[0] + v2[0] * size;
                const pt2Y = p2[1] + v2[1] * size;
                const cornerX = p2[0] + v1[0] * size + v2[0] * size;
                const cornerY = p2[1] + v1[1] * size + v2[1] * size;

                return (
                    <polyline
                        key={`ra-${idx}`}
                        points={`${pt1X},${trY(pt1Y)} ${cornerX},${trY(cornerY)} ${pt2X},${trY(pt2Y)}`}
                        fill="none"
                        stroke="black"
                        strokeWidth={0.2}
                        vectorEffect="non-scaling-stroke"
                    />
                );
            }
            if (el.type === 'label') {
                let offsetX = 0;
                let offsetY = 0;
                // Basic positioning
                if (el.labelPosition === 'top') offsetY = -1.5;
                if (el.labelPosition === 'bottom') offsetY = 1.5;
                if (el.labelPosition === 'left') offsetX = -1.5;
                if (el.labelPosition === 'right') offsetX = 1.5;
                if (el.labelPosition === 'top-left') { offsetX = -1.5; offsetY = -1.5; }
                if (el.labelPosition === 'top-right') { offsetX = 1.5; offsetY = -1.5; }
                if (el.labelPosition === 'bottom-left') { offsetX = -1.5; offsetY = 1.5; }
                if (el.labelPosition === 'bottom-right') { offsetX = 1.5; offsetY = 1.5; }

                return (
                    <text
                        key={`lbl-${idx}`}
                        x={el.point[0] + offsetX}
                        y={trY(el.point[1]) + offsetY}
                        fontSize={el.fontSize || Math.max(1, width / 25)}
                        fontFamily="serif"
                        textAnchor="middle"
                        dominantBaseline="middle"
                        fill="black"
                    >
                        {el.text}
                    </text>
                );
            }
            if (el.type === 'arc') {
                const cx = el.center[0];
                const cy = el.center[1];
                const r = el.radius;
                // Convert degrees to radians.
                // Note: SVG draws paths from start to end, mathematical angles are counter-clockwise from 3 o'clock.
                const startRad = (el.startAngle !== undefined ? el.startAngle : el.start_angle) * Math.PI / 180;
                const endRad = (el.endAngle !== undefined ? el.endAngle : el.end_angle) * Math.PI / 180;

                const startX = cx + r * Math.cos(startRad);
                const startY = cy + r * Math.sin(startRad);
                const endX = cx + r * Math.cos(endRad);
                const endY = cy + r * Math.sin(endRad);

                const largeArcFlag = (el.endAngle !== undefined ? el.endAngle : el.end_angle) - (el.startAngle !== undefined ? el.startAngle : el.start_angle) > 180 ? 1 : 0;
                const sweepFlag = 0; // Negative Y inversion means sweep flag is usually 0 for CCW visual

                return (
                    <path
                        key={`arc-${idx}`}
                        d={`M ${startX} ${trY(startY)} A ${r} ${r} 0 ${largeArcFlag} ${sweepFlag} ${endX} ${trY(endY)}`}
                        fill={el.fill || 'none'}
                        stroke="black"
                        strokeWidth={0.5}
                        strokeDasharray={el.style === 'dashed' ? '2,2' : 'none'}
                        vectorEffect="non-scaling-stroke"
                    />
                );
            }
            if (el.type === 'tick') {
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
            }
            if (el.type === 'point') {
                return (
                    <circle
                        key={`pt-${idx}`}
                        cx={el.point[0]}
                        cy={trY(el.point[1])}
                        r={0.4}
                        fill="black"
                    />
                );
            }
            return null;
        })}
      </svg>
    </div>
  );
}
