// PROFILE-GEOMETRY-V3
using System;
using System.Collections.Generic;
using System.Linq;

public readonly record struct Point2(double X,double Y);

public static class ProfileGeometry
{
    public static IReadOnlyList<Point2> RegularPolygon(int n, Point2 c, double r, double phase=-Math.PI/2)
    {
        if(n<3) throw new ArgumentOutOfRangeException(nameof(n));
        return Enumerable.Range(0,n)
            .Select(j => {
                var t=phase+2*Math.PI*j/n;
                return new Point2(c.X+r*Math.Cos(t),c.Y+r*Math.Sin(t));
            }).ToArray();
    }

    public static double HyperplaneDistance(double[] x,double[] a,double b)
    {
        if(x.Length!=a.Length) throw new ArgumentException("ambient dimension mismatch");
        var dot=x.Zip(a,(xi,ai)=>xi*ai).Sum();
        var n2=a.Sum(ai=>ai*ai);
        if(n2==0) throw new ArgumentException("zero hyperplane normal");
        return Math.Abs(dot-b)/Math.Sqrt(n2);
    }

    public static double[] ProjectToHyperplane(double[] x,double[] a,double b)
    {
        var n2=a.Sum(ai=>ai*ai);
        if(n2==0) throw new ArgumentException("zero hyperplane normal");
        var dot=x.Zip(a,(xi,ai)=>xi*ai).Sum();
        var alpha=(dot-b)/n2;
        return x.Zip(a,(xi,ai)=>xi-alpha*ai).ToArray();
    }
}
