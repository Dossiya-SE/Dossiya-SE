# GEOMETRIC-README-V2
using LinearAlgebra

regular_polygon(n,c,r; phase=-pi/2) = [
    (c[1]+r*cos(phase+2pi*j/n), c[2]+r*sin(phase+2pi*j/n)) for j in 0:n-1
]

function project_hyperplane(x,a,b)
    @assert norm(a) > 0
    x - ((dot(a,x)-b)/dot(a,a))*a
end

# Used conceptually by coupled-network and graph→viability layouts.
power_plane = ([0.0,0.0,0.0], [1.0 0.15; 0.0 1.0; 0.0 0.0])
transport_plane = ([0.0,0.0,1.0], [1.0 0.15; 0.0 1.0; 0.0 0.0])
