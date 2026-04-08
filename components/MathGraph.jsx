"use client";

import React, { useEffect, useRef, useState } from 'react';

export default function MathGraph({ data }) {
  const boardRef = useRef(null);
  const boardObj = useRef(null);
  const [JXG, setJXG] = useState(null);

  useEffect(() => {
    import('jsxgraph').then((jxg) => {
        setJXG(jxg.default);
    });
  }, []);

  useEffect(() => {
    if (!data || !data.elements || !boardRef.current || !JXG) return;

    // Calculate bounding box based on data
    let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;

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

    let width = maxX - minX;
    let height = maxY - minY;

    if (width === 0 || !isFinite(width)) { width = 10; minX = -5; maxX = 5; }
    if (height === 0 || !isFinite(height)) { height = 10; minY = -5; maxY = 5; }

    const paddingX = width * 0.15 || 5;
    const paddingY = height * 0.15 || 5;

    // Initialize the JSXGraph board
    JXG.Options.text.useMathJax = true;
    JXG.Options.text.display = 'html';

    // Check if board already exists, if so clear it, else create
    if (boardObj.current) {
        JXG.JSXGraph.freeBoard(boardObj.current);
    }

    boardObj.current = JXG.JSXGraph.initBoard(boardRef.current.id, {
      boundingbox: [minX - paddingX, maxY + paddingY, maxX + paddingX, minY - paddingY],
      axis: false,
      grid: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });

    const board = boardObj.current;

    // Render elements
    data.elements.forEach(el => {
      if (el.type === 'line') {
        if (el.points) {
           for (let i = 0; i < el.points.length - 1; i++) {
              board.create('segment', [el.points[i], el.points[i+1]], {
                  strokeColor: 'black',
                  strokeWidth: 1,
                  dash: el.style === 'dashed' ? 2 : 0,
                  fixed: true
              });
           }
        } else if (el.point1 && el.point2) {
            board.create('segment', [el.point1, el.point2], {
                strokeColor: 'black',
                strokeWidth: 1,
                dash: el.style === 'dashed' ? 2 : 0,
                fixed: true
            });
        }
      } else if (el.type === 'polygon' || el.type === 'sector' || el.type === 'shaded_region') {
          if (el.points && el.points.length >= 3) {
              const pts = el.points.map(p => board.create('point', p, {visible: false}));
              board.create('polygon', pts, {
                  fillColor: el.fill || (el.type === 'polygon' ? 'none' : '#e5e7eb'),
                  borders: { strokeColor: el.type === 'polygon' ? 'black' : 'none', strokeWidth: 1 },
                  hasInnerBorders: false,
                  vertices: { visible: false }
              });
          }
      } else if (el.type === 'arc') {
           const cx = el.center[0], cy = el.center[1], r = el.radius;
           const startA = (el.startAngle !== undefined ? el.startAngle : el.start_angle) * Math.PI / 180;
           const endA = (el.endAngle !== undefined ? el.endAngle : el.end_angle) * Math.PI / 180;

           const p1 = board.create('point', [cx, cy], {visible: false});
           const p2 = board.create('point', [cx + r * Math.cos(startA), cy + r * Math.sin(startA)], {visible: false});
           const p3 = board.create('point', [cx + r * Math.cos(endA), cy + r * Math.sin(endA)], {visible: false});

           board.create('arc', [p1, p2, p3], {
               strokeColor: 'black',
               strokeWidth: 1,
               dash: el.style === 'dashed' ? 2 : 0
           });
      } else if (el.type === 'point') {
           board.create('point', el.point, {
               size: 2,
               name: '',
               fillColor: 'black',
               strokeColor: 'black',
               fixed: true
           });
      } else if (el.type === 'label') {
           // Basic positioning
           let align = 'middle';
           let valAlign = 'middle';

           // parse position strings roughly
           if (el.labelPosition) {
              if (el.labelPosition.includes('top')) valAlign = 'bottom';
              if (el.labelPosition.includes('bottom')) valAlign = 'top';
              if (el.labelPosition.includes('left')) align = 'right';
              if (el.labelPosition.includes('right')) align = 'left';
           }

           // Format text for MathJax (wrap in inline math if not already)
           let txt = el.text;
           if (!txt.includes('$') && !txt.includes('\\\\')) {
               txt = `\\(${txt}\\)`;
           } else {
               txt = '\\(' + txt.replace(/\$/g, '') + '\\)';
           }

           board.create('text', [el.point[0], el.point[1], txt], {
               fontSize: el.fontSize ? Math.max(12, el.fontSize * 5) : 16,
               anchorX: align,
               anchorY: valAlign,
               cssClass: 'math-label',
               useMathJax: true,
               parse: false
           });
      } else if (el.type === 'right_angle') {
          const p2 = el.point || el.vertex;
          let p1, p3;
          if (el.line1 && el.line2) {
              p1 = el.line1[1]; p3 = el.line2[1];
          } else if (el.point1 && el.point2) {
              p1 = el.point1; p3 = el.point2;
          }
          if (p1 && p2 && p3) {
              const pt1 = board.create('point', p1, {visible: false});
              const pt2 = board.create('point', p2, {visible: false});
              const pt3 = board.create('point', p3, {visible: false});
              board.create('angle', [pt1, pt2, pt3], {
                  type: 'sectordot',
                  dotVisible: true,
                  radius: el.size || 1.5,
                  fillColor: 'none',
                  strokeColor: 'black'
              });
          }
      } else if (el.type === 'tick') {
           if (el.p1 && el.p2) {
               const seg = board.create('segment', [el.p1, el.p2], {visible: false});
               // Create a tick manually using a small segment if count is 2
               const midX = (el.p1[0] + el.p2[0]) / 2;
               const midY = (el.p1[1] + el.p2[1]) / 2;

               const dx = el.p2[0] - el.p1[0];
               const dy = el.p2[1] - el.p1[1];
               const len = Math.sqrt(dx * dx + dy * dy);

               const nx = -dy / len;
               const ny = dx / len;

               const tickLen = 0.8;

               if (el.count === 1 || !el.count) {
                   const t1 = board.create('point', [midX - nx * tickLen, midY - ny * tickLen], {visible: false});
                   const t2 = board.create('point', [midX + nx * tickLen, midY + ny * tickLen], {visible: false});
                   board.create('segment', [t1, t2], {strokeColor: 'black', strokeWidth: 1});
               } else if (el.count === 2) {
                   const sepX = (dx / len) * 0.4;
                   const sepY = (dy / len) * 0.4;

                   const t1a = board.create('point', [midX - sepX - nx * tickLen, midY - sepY - ny * tickLen], {visible: false});
                   const t1b = board.create('point', [midX - sepX + nx * tickLen, midY - sepY + ny * tickLen], {visible: false});
                   board.create('segment', [t1a, t1b], {strokeColor: 'black', strokeWidth: 1});

                   const t2a = board.create('point', [midX + sepX - nx * tickLen, midY + sepY - ny * tickLen], {visible: false});
                   const t2b = board.create('point', [midX + sepX + nx * tickLen, midY + sepY + ny * tickLen], {visible: false});
                   board.create('segment', [t2a, t2b], {strokeColor: 'black', strokeWidth: 1});
               }
           } else if (el.point && el.angle !== undefined) {
               const angleRad = el.angle * Math.PI / 180;
               const tickLen = 1.5;

               const dx = Math.cos(angleRad) * tickLen;
               const dy = Math.sin(angleRad) * tickLen;

               const midX = el.point[0];
               const midY = el.point[1];

               if (el.count === 2) {
                   const sepDirRad = angleRad + Math.PI/2;
                   const sepX = Math.cos(sepDirRad) * 0.8;
                   const sepY = Math.sin(sepDirRad) * 0.8;

                   const t1a = board.create('point', [midX - sepX - dx, midY - sepY - dy], {visible: false});
                   const t1b = board.create('point', [midX - sepX + dx, midY - sepY + dy], {visible: false});
                   board.create('segment', [t1a, t1b], {strokeColor: 'black', strokeWidth: 1});

                   const t2a = board.create('point', [midX + sepX - dx, midY + sepY - dy], {visible: false});
                   const t2b = board.create('point', [midX + sepX + dx, midY + sepY + dy], {visible: false});
                   board.create('segment', [t2a, t2b], {strokeColor: 'black', strokeWidth: 1});
               } else {
                   const t1 = board.create('point', [midX - dx, midY - dy], {visible: false});
                   const t2 = board.create('point', [midX + dx, midY + dy], {visible: false});
                   board.create('segment', [t1, t2], {strokeColor: 'black', strokeWidth: 1});
               }
           }
      } else if (el.type === 'path') {
           // JSXGraph doesn't have an exact equivalent to arbitrary SVG paths but curves can simulate it,
           // or we can just append it as generic SVG text to the board if it's very complex.
           // A simple approach is adding it as a custom element or curve.
           // For path we will try to add an HTML element with an SVG overlay or use board.create('curve')
           // We will map simple path segments if we could parse `el.d`, but usually it's better to just use JSXGraph's `curve` or just an SVG wrapper.
           // Since JSXGraph runs its own SVG renderer, we can inject a primitive:
           board.create('text', [0, 0, `<svg viewBox="0 0 100 100" style="position:absolute; width:100%; height:100%; pointer-events:none;"><path d="${el.d}" fill="${el.fill || 'none'}" stroke="${el.stroke || 'black'}" stroke-width="0.5" transform="scale(1, -1)" /></svg>`], {
               visible: false // This is hacky, so let's stick to parsing if needed. Actually we'll skip arbitrary path for JSXGraph unless converted to geometry.
           });
      }
    });

    // trigger mathjax render if available
    if (window.MathJax) {
        if (window.MathJax.typesetPromise) window.MathJax.typesetPromise();
    }

    return () => {
      if (boardObj.current && JXG) {
         JXG.JSXGraph.freeBoard(boardObj.current);
         boardObj.current = null;
      }
    };
  }, [data, JXG]);

  // generate deterministic id based on array length if possible, or fallback to random
  const idRef = useRef(`jxgbox-${Math.random().toString(36).substr(2, 9)}`);

  return (
    <div className="w-full max-w-[500px] bg-white p-4 my-4 border border-gray-200">
      <div
         id={idRef.current}
         ref={boardRef}
         className="jxgbox"
         style={{ width: '100%', aspectRatio: '1/1' }}
      />
    </div>
  );
}
