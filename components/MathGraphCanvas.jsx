"use client";
import React, { useEffect, useRef } from 'react';

const normalizeVector = (dx, dy) => {
  const len = Math.sqrt(dx * dx + dy * dy);
  if (len === 0) return [0, 0];
  return [dx / len, dy / len];
};

export default function MathGraphCanvas({ data }) {
  const canvasRef = useRef(null);

  useEffect(() => {
    if (!data || !data.elements || !canvasRef.current) return;
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');

    // Calculate bounding box
    let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;

    const updateBounds = (x, y) => {
      if (x < minX) minX = x;
      if (x > maxX) maxX = x;
      if (y < minY) minY = y;
      if (y > maxY) maxY = y;
    };

    data.elements.forEach(el => {
      if (el.point) updateBounds(el.point[0], el.point[1]);
      if (el.points) el.points.forEach(pt => updateBounds(pt[0], pt[1]));
      if (el.center) {
        updateBounds(el.center[0] - (el.radius || 0), el.center[1] - (el.radius || 0));
        updateBounds(el.center[0] + (el.radius || 0), el.center[1] + (el.radius || 0));
      }
      if (el.type === 'tick' && el.p1 && el.p2) {
          updateBounds(el.p1[0], el.p1[1]);
          updateBounds(el.p2[0], el.p2[1]);
      }
      if (el.type === 'right_angle' && (el.point || el.vertex)) {
          const p = el.point || el.vertex;
          updateBounds(p[0], p[1]);
      }
    });

    let w = maxX - minX;
    let h = maxY - minY;
    if (w === 0 || !isFinite(w)) { w = 10; minX = -5; maxX = 5; }
    if (h === 0 || !isFinite(h)) { h = 10; minY = -5; maxY = 5; }

    const padX = w * 0.2 || 5;
    const padY = h * 0.2 || 5;

    const viewW = w + padX * 2;
    const viewH = h + padY * 2;
    const mathMinX = minX - padX;
    const mathMaxY = maxY + padY;

    // Canvas scaling to match CSS size (avoid blur on high DPI)
    const scale = window.devicePixelRatio || 1;
    const cssWidth = 500;
    const cssHeight = (viewH / viewW) * cssWidth;

    canvas.width = cssWidth * scale;
    canvas.height = cssHeight * scale;
    canvas.style.width = `${cssWidth}px`;
    canvas.style.height = `${cssHeight}px`;

    ctx.scale(scale, scale);
    ctx.clearRect(0, 0, cssWidth, cssHeight);

    // Mapping math coords to canvas coords
    const trX = (x) => ((x - mathMinX) / viewW) * cssWidth;
    const trY = (y) => ((mathMaxY - y) / viewH) * cssHeight;
    const trScale = cssWidth / viewW;

    ctx.lineWidth = 1;
    ctx.strokeStyle = 'black';
    ctx.fillStyle = 'black';

    // Helper for rendering
    data.elements.forEach(el => {
      ctx.beginPath();
      if (el.type === 'line') {
        if (el.points) {
          ctx.moveTo(trX(el.points[0][0]), trY(el.points[0][1]));
          for (let i = 1; i < el.points.length; i++) {
             ctx.lineTo(trX(el.points[i][0]), trY(el.points[i][1]));
          }
        } else if (el.point1 && el.point2) {
          ctx.moveTo(trX(el.point1[0]), trY(el.point1[1]));
          ctx.lineTo(trX(el.point2[0]), trY(el.point2[1]));
        }
        if (el.style === 'dashed') ctx.setLineDash([5, 5]);
        else ctx.setLineDash([]);
        ctx.stroke();
      } else if (el.type === 'polygon' || el.type === 'sector' || el.type === 'shaded_region') {
         if (el.points) {
            ctx.moveTo(trX(el.points[0][0]), trY(el.points[0][1]));
            for (let i = 1; i < el.points.length; i++) {
               ctx.lineTo(trX(el.points[i][0]), trY(el.points[i][1]));
            }
            ctx.closePath();
            if (el.type !== 'polygon') {
               ctx.fillStyle = el.fill || '#e5e7eb';
               ctx.fill();
            }
            if (el.type === 'polygon' || el.stroke) {
               ctx.stroke();
            }
            ctx.fillStyle = 'black'; // reset
         } else if (el.center && el.radius) {
            const cx = trX(el.center[0]);
            const cy = trY(el.center[1]);
            const r = el.radius * trScale;
            // Math angles are CCW from East. Canvas angles are CW.
            const startA = -(el.startAngle || el.start_angle) * Math.PI / 180;
            const endA = -(el.endAngle || el.end_angle) * Math.PI / 180;

            ctx.moveTo(cx, cy);
            // arc(x, y, radius, startAngle, endAngle, counterclockwise)
            // canvas uses inverted Y so to draw CCW visually we need CCW flag
            ctx.arc(cx, cy, r, startA, endA, true);
            ctx.closePath();

            ctx.fillStyle = el.fill || '#e5e7eb';
            ctx.fill();
            ctx.stroke();
            ctx.fillStyle = 'black';
         }
      } else if (el.type === 'arc') {
         const cx = trX(el.center[0]);
         const cy = trY(el.center[1]);
         const r = el.radius * trScale;
         const startA = -(el.startAngle || el.start_angle) * Math.PI / 180;
         const endA = -(el.endAngle || el.end_angle) * Math.PI / 180;

         if (el.style === 'dashed') ctx.setLineDash([5, 5]);
         else ctx.setLineDash([]);
         ctx.arc(cx, cy, r, startA, endA, true);
         ctx.stroke();
         ctx.setLineDash([]);
      } else if (el.type === 'tick') {
         const tickLen = 8;
         if (el.p1 && el.p2) {
             const midX = (el.p1[0] + el.p2[0]) / 2;
             const midY = (el.p1[1] + el.p2[1]) / 2;
             const dx = el.p2[0] - el.p1[0];
             const dy = el.p2[1] - el.p1[1];
             const len = Math.sqrt(dx*dx + dy*dy);
             const nx = -dy / len;
             const ny = dx / len;

             const cx = trX(midX);
             const cy = trY(midY);
             // Canvas normal vector
             const cnx = nx;
             const cny = -ny; // negate Y for canvas

             if (el.count === 1 || !el.count) {
                 ctx.moveTo(cx - cnx*tickLen, cy - cny*tickLen);
                 ctx.lineTo(cx + cnx*tickLen, cy + cny*tickLen);
             } else if (el.count === 2) {
                 const sx = (dx/len)*3;
                 const sy = -(dy/len)*3;
                 ctx.moveTo(cx - sx - cnx*tickLen, cy - sy - cny*tickLen);
                 ctx.lineTo(cx - sx + cnx*tickLen, cy - sy + cny*tickLen);
                 ctx.moveTo(cx + sx - cnx*tickLen, cy + sy - cny*tickLen);
                 ctx.lineTo(cx + sx + cnx*tickLen, cy + sy + cny*tickLen);
             }
             ctx.stroke();
         } else if (el.point && el.angle !== undefined) {
             const angleRad = -el.angle * Math.PI / 180;
             const cx = trX(el.point[0]);
             const cy = trY(el.point[1]);

             const dx = Math.cos(angleRad) * tickLen;
             const dy = Math.sin(angleRad) * tickLen;

             if (el.count === 2) {
                 const sepA = angleRad + Math.PI/2;
                 const sx = Math.cos(sepA) * 3;
                 const sy = Math.sin(sepA) * 3;
                 ctx.moveTo(cx - sx - dx, cy - sy - dy);
                 ctx.lineTo(cx - sx + dx, cy - sy + dy);
                 ctx.moveTo(cx + sx - dx, cy + sy - dy);
                 ctx.lineTo(cx + sx + dx, cy + sy + dy);
             } else {
                 ctx.moveTo(cx - dx, cy - dy);
                 ctx.lineTo(cx + dx, cy + dy);
             }
             ctx.stroke();
         }
      } else if (el.type === 'right_angle') {
          const p2 = el.point || el.vertex;
          let p1, p3;
          if (el.line1 && el.line2) { p1 = el.line1[1]; p3 = el.line2[1]; }
          else if (el.point1 && el.point2) { p1 = el.point1; p3 = el.point2; }

          const size = (el.size || 1.5);
          const v1 = normalizeVector(p1[0] - p2[0], p1[1] - p2[1]);
          const v2 = normalizeVector(p3[0] - p2[0], p3[1] - p2[1]);

          const px = trX(p2[0]);
          const py = trY(p2[1]);
          // scale vectors
          const sv1x = v1[0] * size * trScale;
          const sv1y = -v1[1] * size * trScale;
          const sv2x = v2[0] * size * trScale;
          const sv2y = -v2[1] * size * trScale;

          ctx.moveTo(px + sv1x, py + sv1y);
          ctx.lineTo(px + sv1x + sv2x, py + sv1y + sv2y);
          ctx.lineTo(px + sv2x, py + sv2y);
          ctx.stroke();
      } else if (el.type === 'point') {
          ctx.arc(trX(el.point[0]), trY(el.point[1]), 3, 0, Math.PI*2);
          ctx.fill();
      } else if (el.type === 'label') {
          let offsetX = 0;
          let offsetY = 0;
          const offScale = 15;
          if (el.labelPosition) {
              if (el.labelPosition.includes('top')) offsetY = -offScale;
              if (el.labelPosition.includes('bottom')) offsetY = offScale;
              if (el.labelPosition.includes('left')) offsetX = -offScale;
              if (el.labelPosition.includes('right')) offsetX = offScale;
          }

          const txt = el.text.replace(/\$/g, '').replace(/\\/g, '');
          ctx.font = `${el.fontSize ? Math.max(12, el.fontSize*12) : 16}px serif`;
          ctx.textAlign = "center";
          ctx.textBaseline = "middle";
          ctx.fillText(txt, trX(el.point[0]) + offsetX, trY(el.point[1]) + offsetY);
      }
    });
  }, [data]);

  return (
    <div className="w-full max-w-[500px] bg-white p-4 my-4 flex justify-center border border-gray-200 shadow-sm">
      <canvas ref={canvasRef} />
    </div>
  );
}
