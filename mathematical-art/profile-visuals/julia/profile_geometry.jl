# PROFILE-GEOMETRY-V3
using LinearAlgebra

regular_polygon(n::Integer, c::NTuple{2,<:Real}, r::Real; phase=π/2) = [
    (c[1] + r*cos(phase + 2π*j/n), c[2] + r*sin(phase + 2π*j/n))
    for j in 0:n-1
]

struct AffineFlat{T<:Real}
    x0::Vector{T}
    basis::Matrix{T}
    function AffineFlat(x0::AbstractVector{T}, basis::AbstractMatrix{T}) where {T<:Real}
        rank(basis) == size(basis,2) || error("basis vectors must be linearly independent")
        length(x0) == size(basis,1) || error("ambient dimension mismatch")
        new{T}(collect(x0), Matrix(basis))
    end
end

dimension(F::AffineFlat) = size(F.basis,2)

function project(F::AffineFlat, x::AbstractVector)
    Q = Matrix(qr(F.basis).Q)[:,1:dimension(F)]
    F.x0 + Q * (Q' * (x - F.x0))
end

function project_hyperplane(x::AbstractVector, a::AbstractVector, b::Real)
    dot(a,a) > 0 || error("hyperplane normal must be nonzero")
    x - ((dot(a,x)-b)/dot(a,a))*a
end

hyperplane_distance(x,a,b) = abs(dot(a,x)-b)/norm(a)

ellipse_point(c,a,b,t) = (c[1] + a*cos(t), c[2] + b*sin(t))

# Reference invariant used by the profile visuals:
# x - project_hyperplane(x,a,b) is parallel to a.
function projection_invariant(x,a,b; atol=1e-10)
    p = project_hyperplane(x,a,b)
    abs(dot(a,p)-b) <= atol
end
