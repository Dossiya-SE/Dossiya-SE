// GEOMETRIC-README-V2
using System;
using System.Linq;
public readonly record struct Point2(double X,double Y);
public static class ProfileGeometry {
 public static Point2[] RegularPolygon(int n,double cx,double cy,double r) =>
   Enumerable.Range(0,n).Select(j => {
     var t=-Math.PI/2+2*Math.PI*j/n;
     return new Point2(cx+r*Math.Cos(t),cy+r*Math.Sin(t));
   }).ToArray();
 public static double[] ProjectHyperplane(double[] x,double[] a,double b) {
   var aa=a.Sum(v=>v*v); if(aa==0) throw new ArgumentException("a must be nonzero");
   var s=(x.Zip(a,(xi,ai)=>xi*ai).Sum()-b)/aa;
   return x.Zip(a,(xi,ai)=>xi-s*ai).ToArray();
 }
}