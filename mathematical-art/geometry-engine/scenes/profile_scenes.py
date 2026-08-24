"""Manim scenes downstream of the verified geometry source layer."""

from __future__ import annotations
import numpy as np
from manim import BLUE, GOLD, GREEN, TEAL, Create, FadeIn, FadeOut, MathTex, Scene, Surface, Text, ThreeDScene, VGroup, Write
from profile_geometry import torus_point, verify_torus_geometry


class VerifiedDifferentialGeometryScene(ThreeDScene):
    def construct(self) -> None:
        report = verify_torus_geometry()
        if not report["passed"]:
            raise RuntimeError(f"fail-closed geometry gate: {report}")
        surface = Surface(lambda u, v: torus_point(u, v), u_range=[0, 2*np.pi], v_range=[0, 2*np.pi], resolution=(48, 32)).set_fill(BLUE, opacity=0.68)
        formula = MathTex(r"g_{\alpha\beta}=\partial_\alpha\mathbf r\cdot\partial_\beta\mathbf r").scale(0.65)
        self.set_camera_orientation(phi=65*np.pi/180, theta=-35*np.pi/180)
        self.play(Create(surface))
        self.add_fixed_in_frame_mobjects(formula)
        formula.to_corner(np.array([-1.0, 1.0, 0.0]))
        self.play(Write(formula))
        self.begin_ambient_camera_rotation(rate=0.08)
        self.wait(4)


class ProfileSignatureScene(Scene):
    def construct(self) -> None:
        stages = [(MathTex(r"\dot{\mathbf x}=A\mathbf x+B\mathbf u"), BLUE),
                  (Text("Coupled systems"), TEAL), (Text("Dynamics"), GREEN), (Text("Geometry"), GOLD)]
        current = None
        for obj, color in stages:
            obj.set_color(color)
            if current is None:
                self.play(Write(obj))
            else:
                self.play(FadeOut(current), FadeIn(obj))
            current = obj
        self.play(FadeOut(current))
        group = VGroup(Text("Dossiya Dakou").scale(1.25),
                       Text("MATHEMATICS · PHYSICS · COMPUTATION · SUSTAINABILITY · FINANCE").scale(0.38)).arrange(np.array([0.0, -1.0, 0.0]), buff=0.35)
        self.play(Write(group))
        self.wait(2)
