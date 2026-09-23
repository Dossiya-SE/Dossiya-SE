# Motion Contract V1

**Contract ID:** DOSS-MOTION-V1  
**Principle:** motion must encode mathematical, physical, computational or navigational meaning.

## Allowed classes

- Mathematical evolution: Frenet frame, geodesic, heat flow, trajectory.
- System-dynamics explanation: disturbance, control, restoration, interface activation.
- Structural reveal: evidence → model → verification; graph → dynamics → viability.
- Camera motion: only with fixed geometry and a caption stating that motion is not physical time.

## Forbidden motion

No decorative particles, random jitter, flashing emphasis, perpetual motion that obscures reading, or motion that implies dynamics/validation when only presentation changes.

## Required motion variable

```text
t_phys   physical time
t_model  model/simulation time
s        curve/geodesic parameter
lambda   continuation/control parameter
theta    camera/orbit parameter
tau_ui   presentation/reveal time
```

## Determinism

Generated motion must fix source data/geometry, random seed when needed, frame count, timing law, viewport/camera and palette.

## Accessibility

Respect reduced motion on the web. Keep a complete static master. No essential information may exist only in motion.

## Acceptance

```text
MOTION_VARIABLE_DEFINED
AND STATIC_MASTER_COMPLETE
AND FRAME_DETERMINISM_PASS
AND SEMANTIC_INVARIANCE_PASS
AND REDUCED_MOTION_PASS
AND CAPTION_BOUNDARY_PASS
```
