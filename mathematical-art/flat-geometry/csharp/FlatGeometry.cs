// FLAT-GEOMETRY-V1
// Engineering integration mirror: C# / SVG.
using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;

public readonly record struct Point2(double X, double Y);

public static class FlatGeometry
{
    public static IReadOnlyList<Point2> RegularPolygon(int n, double cx, double cy, double r)
    {
        if (n < 3) throw new ArgumentOutOfRangeException(nameof(n));
        return Enumerable.Range(0, n).Select(j =>
        {
            var t = Math.PI / 2.0 + 2.0 * Math.PI * j / n;
            return new Point2(cx + r * Math.Cos(t), cy - r * Math.Sin(t));
        }).ToArray();
    }

    public static double HyperplaneDistance(double[] x, double[] a, double b)
    {
        if (x.Length != a.Length) throw new ArgumentException("ambient dimensions must agree");
        var dot = x.Zip(a, (xi, ai) => xi * ai).Sum();
        var norm = Math.Sqrt(a.Sum(ai => ai * ai));
        if (norm == 0) throw new ArgumentException("a must be nonzero");
        return Math.Abs(dot - b) / norm;
    }

    public static string PolygonSvg(int n, double cx, double cy, double r)
    {
        var points = string.Join(" ", RegularPolygon(n, cx, cy, r)
            .Select(p => string.Create(CultureInfo.InvariantCulture, $"{p.X:F2},{p.Y:F2}")));
        return $"<polygon points=\"{points}\" fill=\"none\" stroke=\"#6D28D9\"/>";
    }
}
