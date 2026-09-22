// FLAT-GEOMETRY-V1
// Interactive web mirror. The GitHub README release remains the deterministic Python SVG.
import React from "react";
import "./flat-geometry.css";

type Pt = [number, number];

function regularPolygon(n: number, cx: number, cy: number, r: number): Pt[] {
  return Array.from({ length: n }, (_, j) => {
    const t = Math.PI / 2 + (2 * Math.PI * j) / n;
    return [cx + r * Math.cos(t), cy - r * Math.sin(t)];
  });
}

const pts = (p: Pt[]) => p.map(([x, y]) => `${x.toFixed(2)},${y.toFixed(2)}`).join(" ");

export function FlatGeometry(): React.JSX.Element {
  const sides = [3, 4, 5, 6, 7, 8, 9, 10];
  return (
    <svg className="flat-geometry" viewBox="0 0 1000 420" role="img" aria-labelledby="fg-title fg-desc">
      <title id="fg-title">Geometry of flats</title>
      <desc id="fg-desc">Regular plane figures, affine flats and a hyperplane distance construction.</desc>
      <text x="32" y="42" className="fg-title">Geometry of Flats</text>
      <g aria-label="regular polygons">
        {sides.map((n, i) => {
          const cx = 85 + (i % 4) * 130;
          const cy = 120 + Math.floor(i / 4) * 120;
          return <polygon key={n} points={pts(regularPolygon(n, cx, cy, 38))} className="fg-math" />;
        })}
      </g>
      <g aria-label="affine flat">
        <line x1="590" y1="120" x2="820" y2="120" className="fg-topology" />
        <polygon points="600,220 810,245 770,310 560,285" className="fg-plane" />
        <text x="565" y="350" className="fg-eq">F = x₀ + span(v₁,…,vₖ)</text>
      </g>
      <g aria-label="hyperplane distance">
        <line x1="860" y1="85" x2="940" y2="320" className="fg-critical" />
        <circle cx="845" cy="230" r="6" className="fg-state" />
        <line x1="845" y1="230" x2="900" y2="208" className="fg-distance" />
      </g>
    </svg>
  );
}
