// PROFILE-GEOMETRY-V3
import React from "react";
import "./profile-geometry.css";

export type Point = [number, number];

export const regularPolygon = (n:number, cx:number, cy:number, r:number, phase=-Math.PI/2):Point[] =>
  Array.from({length:n},(_,j)=>{
    const t=phase+2*Math.PI*j/n;
    return [cx+r*Math.cos(t),cy+r*Math.sin(t)];
  });

const pts=(p:Point[])=>p.map(([x,y])=>`${x.toFixed(2)},${y.toFixed(2)}`).join(" ");

export function AffinePlane({points,className}:{points:Point[];className:string}) {
  return <polygon points={pts(points)} className={className}/>;
}

export function TypedNode({kind,x,y,label}:{kind:"circle"|"triangle"|"square"|"diamond"|"hexagon";x:number;y:number;label:string}) {
  const poly = kind==="triangle" ? regularPolygon(3,x,y,12)
    : kind==="square" ? regularPolygon(4,x,y,11)
    : kind==="diamond" ? regularPolygon(4,x,y,11,0)
    : kind==="hexagon" ? regularPolygon(6,x,y,12)
    : null;
  return <g aria-label={label}>
    {poly ? <polygon points={pts(poly)} className="gv-node"/> : <circle cx={x} cy={y} r="10" className="gv-node"/>}
  </g>;
}

export function ViabilityGeometry() {
  return <svg viewBox="0 0 420 260" className="gv-svg" role="img" aria-label="Viability ellipse with critical hyperplane and orthogonal resilience margin">
    <ellipse cx="205" cy="130" rx="130" ry="82" className="gv-viable"/>
    <line x1="120" y1="225" x2="315" y2="35" className="gv-critical"/>
    <circle cx="160" cy="74" r="6" className="gv-state"/>
    <line x1="160" y1="74" x2="207" y2="120" className="gv-projection"/>
  </svg>;
}

export function StageMarker({stage,x,label}:{stage:number;x:number;label:string}) {
  const n=Math.min(9,stage+2);
  return <g aria-label={label}>
    <polygon points={pts(regularPolygon(n,x,70,22))} className="gv-stage"/>
    <text x={x} y={112} textAnchor="middle">{label}</text>
  </g>;
}
