// PROFILE-GEOMETRY-V3
package main

import (
  "fmt"
  "math"
  "strings"
)

type Point struct{ X,Y float64 }

func RegularPolygon(n int,c Point,r,phase float64) []Point {
  p:=make([]Point,n)
  for j:=0;j<n;j++{
    t:=phase+2*math.Pi*float64(j)/float64(n)
    p[j]=Point{c.X+r*math.Cos(t),c.Y+r*math.Sin(t)}
  }
  return p
}

func HyperplaneDistance(x,a []float64,b float64) float64 {
  var dot,n2 float64
  for i:=range x { dot+=a[i]*x[i]; n2+=a[i]*a[i] }
  if n2==0 { panic("zero hyperplane normal") }
  return math.Abs(dot-b)/math.Sqrt(n2)
}

func SVGPolygon(p []Point) string {
  s:=make([]string,len(p))
  for i,q:=range p { s[i]=fmt.Sprintf("%.2f,%.2f",q.X,q.Y) }
  return "<polygon points=\"" + strings.Join(s," ") + "\"/>"
}

func main(){
  fmt.Println(SVGPolygon(RegularPolygon(6,Point{50,50},24,-math.Pi/2)))
}
