#!/usr/bin/env julia
# SCIENTIFIC-GEOMETRY-V3 independent numerical verification.
using LinearAlgebra
using Printf
using TOML

root = normpath(joinpath(@__DIR__, "..", "..", ".."))
cfg = TOML.parsefile(joinpath(root, "data", "scientific-geometry-v3.toml"))
mkpath(joinpath(root, "artifacts"))

vec(x) = Float64.(x)

const CANONICAL_SIG_DIGITS = 14
const CANONICAL_ZERO_TOL = 1e-14

function canonical_float(x)
    y = Float64(x)
    isfinite(y) || error("non-finite Julia audit value")
    abs(y) < CANONICAL_ZERO_TOL && return "0.0"
    @sprintf("%.14g", y)
end

function plane_matrix(section)
    hcat(vec(section["basis1"]), vec(section["basis2"]))
end

function projection(state, normal, b)
    x = vec(state)
    a = vec(normal)
    x - ((dot(a,x)-Float64(b))/dot(a,a))*a
end

function feasible_projection_candidates(vcfg; tol=1e-10)
    x = vec(vcfg["state"])
    rows = vcfg["constraints"]
    candidates = NamedTuple[]
    for (idx,row) in enumerate(rows)
        name = String(row[1])
        a = [Float64(row[2]), Float64(row[3])]
        b = Float64(row[4])
        q = projection(x,a,b)
        feasible = true
        for r in rows
            ar = [Float64(r[2]), Float64(r[3])]
            br = Float64(r[4])
            if dot(ar,q) > br + tol
                feasible = false
                break
            end
        end
        if feasible
            push!(candidates,(index=idx,name=name,a=a,b=b,q=q,distance=norm(q-x)))
        end
    end
    isempty(candidates) && error("no feasible orthogonal boundary projection found")
    candidates
end

P = plane_matrix(cfg["hero"]["power_plane"])
T = plane_matrix(cfg["hero"]["transport_plane"])
rank(P) == 2 || error("power plane rank != 2")
rank(T) == 2 || error("transport plane rank != 2")

Qp = Matrix(qr(P).Q)[:,1:2]
Qt = Matrix(qr(T).Q)[:,1:2]
orth_p = norm(Qp'Qp - Matrix{Float64}(I,2,2))
orth_t = norm(Qt'Qt - Matrix{Float64}(I,2,2))

vcfg = cfg["viability"]
distance_metric = String(vcfg["metric"])
distance_metric == "euclidean_L2" || error("Julia verifier supports viability metric euclidean_L2 only")
x = vec(vcfg["state"])
candidates = feasible_projection_candidates(vcfg)
active = candidates[argmin(getfield.(candidates,:distance))]
q = active.q
a = active.a
b = active.b
boundary_residual = abs(dot(a,q)-b)
tangent = [-a[2], a[1]]
orth_residual = abs(dot(q-x,tangent))
distance = active.distance

orth_p < 1e-12 || error("power QR orthogonality failed")
orth_t < 1e-12 || error("transport QR orthogonality failed")
boundary_residual < 1e-12 || error("viability projection not on active boundary")
orth_residual < 1e-12 || error("viability displacement not normal to active boundary")

target_area = Float64(cfg["projects"]["target_area"])
areas = Float64[]
for n_any in cfg["projects"]["sides"]
    n = Int(n_any)
    r = sqrt(2target_area/(n*sin(2pi/n)))
    push!(areas, n*r^2*sin(2pi/n)/2)
end
maximum(abs.(areas .- target_area)) < 1e-10 || error("equal-area polygon formula failed")

report = joinpath(root, "artifacts", "julia-geometry-check.toml")
open(report, "w") do io
    println(io, "contract_id = \"SCIENTIFIC-GEOMETRY-V3\"")
    println(io, "power_rank = ", rank(P))
    println(io, "transport_rank = ", rank(T))
    println(io, "canonical_significant_digits = ", CANONICAL_SIG_DIGITS)
    println(io, "canonical_zero_tolerance = ", canonical_float(CANONICAL_ZERO_TOL))
    println(io, "distance_metric = \"", distance_metric, "\"")
    println(io, "power_q_orthogonality = ", canonical_float(orth_p))
    println(io, "transport_q_orthogonality = ", canonical_float(orth_t))
    println(io, "active_constraint_index = ", active.index)
    println(io, "active_constraint_name = \"", active.name, "\"")
    println(io, "projection_x = ", canonical_float(q[1]))
    println(io, "projection_y = ", canonical_float(q[2]))
    println(io, "distance = ", canonical_float(distance))
    println(io, "boundary_residual = ", canonical_float(boundary_residual))
    println(io, "orthogonality_residual = ", canonical_float(orth_residual))
    println(io, "max_project_area_error = ", canonical_float(maximum(abs.(areas .- target_area))))
end

println("JULIA GEOMETRY VERIFICATION: PASS")
println("active constraint = ", active.index, " (", active.name, "), projection = ", q, ", distance = ", distance)
