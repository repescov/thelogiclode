from manim import *
import numpy as np

# Configurare format VERTICAL 4K (9:16)
config.pixel_height = 3840
config.pixel_width = 2160
config.frame_height = 16.0
config.frame_width = 9.0
config.background_color = "#111111"

class PiVisual(MovingCameraScene):
    def construct(self):
        # Micșorăm totul cu 5% prin camera frame
        self.camera.frame.scale(1/0.95)
        
        # Culori inversate conform cerinței
        C_D1 = ORANGE
        C_D2 = BLUE
        C_AXIS = GRAY
        C_TEXT = WHITE
        
        # Segment 1 (d=2) - Top
        d1_val = 2.0
        d1_line = Line(LEFT, RIGHT, color=C_D1, stroke_width=8).scale(d1_val/2).shift(UP * 4)
        d1_label = MathTex("d = 2", font_size=50, color=C_D1).next_to(d1_line, UP)
        
        # Segment 2 (d=3) - Bottom
        d2_val = 3.0
        d2_line = Line(LEFT, RIGHT, color=C_D2, stroke_width=8).scale(d2_val/2).shift(DOWN * 2)
        d2_label = MathTex("d = 3", font_size=50, color=C_D2).next_to(d2_line, UP)
        
        self.play(Create(d1_line), Write(d1_label))
        self.play(Create(d2_line), Write(d2_label))
        self.wait(1)
        
        # --- STEP 2: Transform into Circles ---
        circle1 = Circle(radius=d1_val/2, color=C_D1, stroke_width=6).move_to(d1_line)
        circle2 = Circle(radius=d2_val/2, color=C_D2, stroke_width=6).move_to(d2_line)
        
        self.play(
            Create(circle1),
            Rotate(d1_line, angle=2*PI),
            Create(circle2),
            Rotate(d2_line, angle=2*PI),
            run_time=3,
            rate_func=smooth
        )
        self.wait(1)
        
        # --- STEP 3: Number Line ---
        ax_step = 0.8
        axis = NumberLine(
            x_range=[0, 10, 1], length=10 * ax_step, color=C_AXIS,
            include_numbers=True, label_direction=DOWN, font_size=36
        ).move_to(UP * 1)
        
        self.play(Create(axis))
        self.wait(1)

        # --- CUT AND FLATTEN ANIMATION ---
        arc1 = Arc(radius=1.0, start_angle=PI/2, angle=2*PI-0.01, color=C_D1, stroke_width=6).move_to(circle1)
        arc2 = Arc(radius=1.5, start_angle=-PI/2, angle=-2*PI+0.01, color=C_D2, stroke_width=6).move_to(circle2)
        self.add(arc1, arc2)

        trace1 = Line(axis.n2p(0), axis.n2p(2*PI), color=C_D1, stroke_width=10).shift(UP * 0.2)
        trace2 = Line(axis.n2p(0), axis.n2p(3*PI), color=C_D2, stroke_width=10)

        # English labels, dot as decimal separator
        l_label1 = MathTex(r"C = 6.28", font_size=50, color=C_D1).next_to(trace1, UP, buff=0.1)
        l_label2 = MathTex(r"C = 9.42", font_size=50, color=C_D2).move_to(axis.n2p(7)).shift(UP * 0.6+RIGHT*1)

        self.play(ReplacementTransform(arc1, trace1), run_time=3)
        self.play(Write(l_label1))
        self.wait(1)

        # Chain Equality
        eq_mid = MathTex("=", font_size=65, color=WHITE).move_to(UP * 6.5)
        frac1_pos = eq_mid.get_center() + LEFT * 1.5
        frac_line1 = Line(LEFT*0.5, RIGHT*0.5, color=C_D1).move_to(frac1_pos)
        l_sym1 = l_label1[0][2:].copy() 
        d_sym1 = d1_label[0][2:].copy() 

        self.play(
            l_sym1.animate.scale(1.2).next_to(frac_line1, UP, buff=0.2),
            d_sym1.animate.scale(1.2).next_to(frac_line1, DOWN, buff=0.2),
            Create(frac_line1),
            run_time=2
        )

        self.play(ReplacementTransform(arc2, trace2), run_time=3)
        self.play(Write(l_label2))
        self.wait(1)

        frac_line2 = Line(LEFT*0.5, RIGHT*0.5, color=C_D2).next_to(eq_mid, RIGHT, buff=0.6)
        l_copy2 = l_label2[0][2:].copy() 
        d_copy2 = d2_label[0][2:].copy() 

        self.play(
            Write(eq_mid), Create(frac_line2),
            l_copy2.animate.scale(1.2).next_to(frac_line2, UP, buff=0.2).set_color(C_D2),
            d_copy2.animate.scale(1.2).next_to(frac_line2, DOWN, buff=0.2).set_color(C_D2),
            run_time=2
        )
        
        full_chain = VGroup(frac_line1, l_sym1, d_sym1, eq_mid, frac_line2, l_copy2, d_copy2)
        self.wait(2)
        
        # --- STEP 4: Dynamism ---
        d_tracker = ValueTracker(3.0)
        
        # Dynamic elements
        dyn_trace2 = always_redraw(lambda: Line(
            axis.n2p(0), axis.n2p(d_tracker.get_value() * PI), color=C_D2, stroke_width=10
        ))
        
        dyn_circle2 = always_redraw(lambda: Circle(
            radius=d_tracker.get_value()/2, color=C_D2, stroke_width=6
        ).move_to(DOWN * 2))

        dyn_num2 = always_redraw(lambda: MathTex(
            f"{d_tracker.get_value()*PI:.2f}", # Dot separator
            font_size=50, color=C_D2
        ).next_to(frac_line2, UP, buff=0.2).scale(1.2))
        
        dyn_den2 = always_redraw(lambda: MathTex(
            f"{d_tracker.get_value():.1f}", # Dot separator
            font_size=50, color=C_D2
        ).next_to(frac_line2, DOWN, buff=0.2).scale(1.2))

        dyn_l_label_axis = always_redraw(lambda: MathTex(
            f"C = {d_tracker.get_value()*PI:.2f}",
            font_size=50, color=C_D2
        ).move_to(axis.n2p(7)).shift(UP * 0.6 + RIGHT * 1))

        dyn_diameter2 = always_redraw(lambda: Line(
            LEFT, RIGHT, color=C_D2, stroke_width=8
        ).scale(d_tracker.get_value()/2).move_to(DOWN * 2))
        
        d_label_side = ValueTracker(0)
        dyn_d_label_circle = always_redraw(lambda: MathTex(
            f"d = {d_tracker.get_value():.1f}",
            font_size=40, color=C_D2
        ).next_to(dyn_diameter2, UP if d_label_side.get_value() < 0.5 else RIGHT, buff=0.2))

        # Add dynamic elements
        self.add(dyn_trace2, dyn_circle2, dyn_diameter2, dyn_l_label_axis, dyn_d_label_circle, dyn_num2, dyn_den2)
        
        # Remove static objects
        self.remove(circle2, trace2, d2_line, l_label2, d2_label, l_copy2, d_copy2)
        
        # Fade out elements
        self.play(
            FadeOut(trace1), FadeOut(l_label1),
            run_time=0.5
        )

        # Shrink animation (Part 1)
        self.play(d_tracker.animate.set_value(1.8), run_time=3)
        self.wait(0.5)

        # Reposition chain
        static_chain = VGroup(frac_line1, l_sym1, d_sym1, eq_mid, frac_line2)
        const_text = MathTex("= \\text{const}", font_size=65, color=WHITE).next_to(frac_line2, RIGHT, buff=0.3)
        
        self.play(
            static_chain.animate.shift(LEFT * 1.2),
            d_label_side.animate.set_value(1),
            Write(const_text),
            const_text.animate.shift(LEFT * 1.2),
            run_time=2
        )
        self.wait(1)

        # Shrink animation (Part 2)
        self.play(d_tracker.animate.set_value(1.0), run_time=3)
        self.wait(1)

        # --- STEP 5: Revelation ---
        # English: Circumference / Diameter
        pi_def = MathTex(r"\frac{\text{Circumference}}{\text{Diameter}} = \pi", font_size=90, color=WHITE)
        ref_w_def = pi_def.get_width()

        # Robust updater for fixed position
        pi_def.add_updater(lambda m: m.move_to(
            self.camera.frame.get_center() + UP * (self.camera.frame.get_height() * 0.42)
        ).set_width(ref_w_def * (self.camera.frame.get_width() / 9)))

        pi_def.set_opacity(0)
        self.add(pi_def)

        self.play(
            FadeOut(static_chain),
            pi_def.animate.set_opacity(1),
            FadeOut(const_text),
            FadeOut(dyn_circle2), FadeOut(dyn_num2), FadeOut(dyn_den2),
            FadeOut(dyn_diameter2), FadeOut(dyn_d_label_circle), FadeOut(dyn_l_label_axis),
            FadeOut(circle1), FadeOut(d1_line), FadeOut(d1_label),
            run_time=2
        )
        self.wait(1)
        
        # Pi marker on axis
        pi_line = Line(axis.n2p(PI) + UP*0.3, axis.n2p(PI) + DOWN*0.3, color=YELLOW, stroke_width=8)
        pi_text_axis = MathTex(r"\pi", font_size=70, color=YELLOW).next_to(pi_line, UP, buff=0.2)

        # Zoom on axis
        self.play(
            self.camera.frame.animate.move_to(axis.n2p(3.3)).set(width=3),
            Create(pi_line),
            Write(pi_text_axis),
            run_time=2
        )
        self.wait(1)
        
        # Final animation: value appears next to pi
        pi_val_part = MathTex(r" = 3.14159\dots", font_size=70, color=YELLOW)
        pi_val_part.next_to(pi_text_axis, RIGHT, buff=0.1)
        
        # Group and animate shift + scale
        full_group = VGroup(pi_text_axis, pi_val_part)
        
        self.play(
            Write(pi_val_part),
            full_group.animate.shift(LEFT * 1.9).scale(0.55),
            run_time=2.5
        )
        
        self.wait(5)
