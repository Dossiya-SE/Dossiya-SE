// FLAT-GEOMETRY-V1
// Dependency-light geometry mirror: Go.
package main

import (
	"fmt"
	"math"
	"strings"
)

type Point struct{ X, Y float64 }

func regularPolygon(n int, cx, cy, r float64) []Point {
	p := make([]Point, n)
	for j := 0; j < n; j++ {
		t := math.Pi/2 + 2*math.Pi*float64(j)/float64(n)
		p[j] = Point{cx + r*math.Cos(t), cy - r*math.Sin(t)}
	}
	return p
}

func hyperplaneDistance(x, a []float64, b float64) float64 {
	var dot, norm2 float64
	for i := range x {
		dot += a[i] * x[i]
		norm2 += a[i] * a[i]
	}
	if norm2 == 0 { panic("a must be nonzero") }
	return math.Abs(dot-b) / math.Sqrt(norm2)
}

func pointsAttr(p []Point) string {
	out := make([]string, len(p))
	for i, q := range p { out[i] = fmt.Sprintf("%.2f,%.2f", q.X, q.Y) }
	return strings.Join(out, " ")
}

func main() {
	fmt.Println("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 600 220\">")
	for i, n := range []int{3,4,5,6,7,8,9,10} {
		x := 45.0 + float64(i%4)*135
		y := 55.0 + float64(i/4)*105
		fmt.Printf("<polygon points=\"%s\" fill=\"none\" stroke=\"#6D28D9\"/>\n", pointsAttr(regularPolygon(n,x,y,34)))
	}
	fmt.Println("</svg>")
}
