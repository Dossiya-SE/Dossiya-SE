// GEOMETRIC-README-V2
import React from "react";
import "./profile-geometry.css";

export function GeometryFrame({children}:{children:React.ReactNode}) {
  return <svg className="geometry-frame" viewBox="0 0 1600 620" role="img">{children}</svg>;
}
export const Polygon=({points,className}:{points:string,className:string}) =>
  <polygon points={points} className={className}/>;
export const ViabilityEllipse=({cx,cy,rx,ry}:{cx:number,cy:number,rx:number,ry:number}) =>
  <ellipse cx={cx} cy={cy} rx={rx} ry={ry} className="viability"/>;
