# FLAT-GEOMETRY-V1
# Numerical geometry mirror: Julia
using LinearAlgebra
using Printf

regular_polygon(n::Integer, c::Tuple{<:Real,<:Real}, r::Real) = [
    (c[1] + r*cos(2π*j/n + π/2), c[2] + r*sin(2π*j/n + π/2))
    for j in 0:n-1
]

function hyperplane_distance(x::AbstractVector, a::AbstractVector, b::Real)
    @assert length(x) == length(a)
    na = norm(a)
    @assert na > 0 "a must be nonzero"
    return abs(dot(a, x) - b) / na
end

struct AffineFlat
    x0::Vector{Float64}
    basis::Matrix{Float64}
    function AffineFlat(x0, basis)
        B = Matrix{Float64}(basis)
        rank(B) == size(B, 2) || error("basis vectors must be linearly independent")
        length(x0) == size(B, 1) || error("ambient dimensions must agree")
        new(Vector{Float64}(x0), B)
    end
end

dimension(F::AffineFlat) = size(F.basis, 2)
point(F::AffineFlat, λ::AbstractVector) = F.x0 + F.basis*λ

for n in 3:10
    pts = regular_polygon(n, (0.0, 0.0), 1.0)
    @printf("%2d-gon: first vertex = (%.6f, %.6f)\n", n, pts[1]...)
end
