# Verified Geometry Engine — V6

This directory implements the profile rule:

```text
mathematical definition
→ computation
→ invariant/residual verification
→ renderer-neutral exchange
→ renderer-specific presentation
```

A renderer is never the source of mathematical truth.

## Implemented now

- analytic torus parameterization `r(u,v)`;
- coordinate tangent basis `(∂u r, ∂v r)`;
- unit normal;
- first fundamental form `g_{αβ}`;
- analytic Gaussian curvature for the reference torus;
- sampled vertices, normals, and curvature fields;
- fail-closed verification using independent central finite differences;
- renderer-neutral JSON exchange for Manim, PyVista/VTK, Blender, and Three.js consumers;
- Manim source scenes downstream of the verification gate;
- renderer/motion contracts for every major visual exposed in the profile README.

The reference torus is a verification demonstrator. It is **not** evidence that an infrastructure or finance state space is a Riemannian manifold.

## Verification invariants

```math
\|\mathbf n\|=1,\qquad
\mathbf n\cdot\partial_u\mathbf r=0,\qquad
\mathbf n\cdot\partial_v\mathbf r=0,
```

```math
g_{\alpha\beta}=g_{\beta\alpha},\qquad
\det g>0.
```

Analytic partial derivatives are independently checked against central finite differences before the reference geometry is eligible for verified rendering.

## Renderer responsibilities

| Layer | Responsibility |
|---|---|
| `profile_geometry` | mathematical objects and fields |
| `verification.py` | invariant/residual checks |
| `export.py` | renderer-neutral exchange |
| Manim | mathematical motion |
| PyVista/VTK | scientific 3-D |
| Blender | cinematic rendering downstream of verified data |
| Three.js/WebGPU/WebGL | interactive browser rendering |
| adaptive SVG | canonical GitHub summary graphics |

See [`renderer_registry_v6.json`](renderer_registry_v6.json) for the per-profile-part policy.
