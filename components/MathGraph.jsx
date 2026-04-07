import React from 'react';

// Direction vectors for native string parsing in offsets
const DIRECTION_VECTORS = {
  N: [0, -1],
  S: [0, 1],
  E: [1, 0],
  W: [-1, 0],
  NE: [1, -1],
  NW: [-1, -1],
  SE: [1, 1],
  SW: [-1, 1],
};

const normalizeVector = (dx, dy) => {
  const len = Math.sqrt(dx * dx + dy * dy);
  if (len === 0) return [0, 0];
  return [dx / len, dy / len];
};

export default function MathGraph({ data }) {
  // To handle the strict 42x42 coordinates, we will dynamically calculate a viewBox.
  // The SVG viewBox will cover the min and max X, Y coordinates, plus some padding.

  let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;

  Object.values(data.points).forEach(([x, y]) => {
    if (x < minX) minX = x;
    if (x > maxX) maxX = x;
    if (y < minY) minY = y;
    if (y > maxY) maxY = y;
  });

  // Calculate bounding box width and height
  let width = maxX - minX;
  let height = maxY - minY;

  // Add 10% padding so labels don't get clipped
  const paddingX = width * 0.15 || 5;
  const paddingY = height * 0.15 || 5;

  const viewBox = `${minX - paddingX} ${minY - paddingY} ${width + paddingX*2} ${height + paddingY*2}`;

  // Transform a point from domain coordinates to SVG space?
  // SVG natively uses the viewBox, so we just use the exact coordinates.
  // Wait, math coordinates usually have +Y going UP.
  // SVG coordinates have +Y going DOWN.
  // In the JSON, P(0, 42) and Q(0, 0) meant P was the top-left corner in Asymptote (where +Y is up).
  // If we just plot them in SVG, P(0, 42) will be at the bottom.
  // Let's create a transform function to invert Y.

  const trY = (y) => maxY - y + minY;

  return (
    <div className="w-full max-w-[500px] border border-gray-200 bg-white p-4 shadow-sm my-4">
      <svg
        viewBox={viewBox}
        xmlns="http://www.w3.org/2000/svg"
        className="w-full h-auto"
        vectorEffect="non-scaling-stroke"
      >
        {/* Draw Right Angles */}
        {data.right_angles && data.right_angles.map((angle, idx) => {
          const p1 = data.points[angle.p1];
          const p2 = data.points[angle.p2];
          const p3 = data.points[angle.p3];
          const size = angle.size || 1.5;

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
        })}

        {/* Draw Lines */}
        {data.lines.map((line, idx) => {
          // A line can have multiple points "A", "B", "C"
          const pts = line.points.map(ptName => {
             const [x, y] = data.points[ptName];
             return `${x},${trY(y)}`;
          }).join(" ");

          return (
            <polyline
              key={`line-${idx}`}
              points={pts}
              fill="none"
              stroke="black"
              strokeWidth={0.5}
              strokeDasharray={line.style === 'dashed' ? '2,2' : 'none'}
              vectorEffect="non-scaling-stroke"
            />
          );
        })}

        {/* Draw Annotations (Line Labels) */}
        {data.annotations && data.annotations.map((ann, idx) => {
          const p1 = data.points[ann.p1];
          const p2 = data.points[ann.p2];
          const midX = (p1[0] + p2[0]) / 2;
          const midY = (p1[1] + p2[1]) / 2;

          let offsetX = 0;
          let offsetY = 0;
          if (ann.position && DIRECTION_VECTORS[ann.position]) {
              const vec = DIRECTION_VECTORS[ann.position];
              // Scale vector for padding
              offsetX = vec[0] * 1.5;
              // Remember Y is inverted visually!
              // If position says "S" (down mathematically), we want it lower on screen (+Y in SVG)
              // Wait, math S = (0, -1). SVG S = (0, +1). So we just add the vector directly if it's already SVG-oriented?
              // No, let's treat "S" as visually down. S in our map is (0, 1). So Y increases, which is visually down in SVG.
              offsetY = vec[1] * 1.5;
          }

          return (
            <text
              key={`ann-${idx}`}
              x={midX + offsetX}
              y={trY(midY) + offsetY}
              fontSize={1.1}
              fontFamily="serif"
              textAnchor="middle"
              dominantBaseline="middle"
              fill="black"
            >
              {ann.text}
            </text>
          );
        })}

        {/* Draw Vertex Labels */}
        {data.labels.map((lbl, idx) => {
          const pt = data.points[lbl.point];
          let offsetX = 0;
          let offsetY = 0;
          if (lbl.position && DIRECTION_VECTORS[lbl.position]) {
              const vec = DIRECTION_VECTORS[lbl.position];
              offsetX = vec[0] * 2.0;
              offsetY = vec[1] * 2.0;
          }

          return (
            <text
              key={`lbl-${idx}`}
              x={pt[0] + offsetX}
              y={trY(pt[1]) + offsetY}
              fontSize={1.5}
              fontFamily="serif"
              textAnchor="middle"
              dominantBaseline="middle"
              fill="black"
            >
              {lbl.text}
            </text>
          );
        })}
      </svg>
    </div>
  );
}
