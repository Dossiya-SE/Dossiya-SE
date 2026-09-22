// GEOMETRIC-README-V2
package geometry
import ("math";"fmt";"strings")
type Point struct{X,Y float64}
func RegularPolygon(n int,cx,cy,r float64) []Point {
 p:=make([]Point,n)
 for j:=0;j<n;j++ { t:=-math.Pi/2+2*math.Pi*float64(j)/float64(n); p[j]=Point{cx+r*math.Cos(t),cy+r*math.Sin(t)} }
 return p
}
func PointsAttr(p []Point) string { q:=make([]string,len(p)); for i,v:=range p {q[i]=fmt.Sprintf("%.1f,%.1f",v.X,v.Y)}; return strings.Join(q," ") }
