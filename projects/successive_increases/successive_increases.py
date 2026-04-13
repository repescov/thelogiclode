from manim import *

# Configuration for VERTICAL 4K format (9:16)
config.pixel_height = 3840
config.pixel_width = 2160
config.frame_height = 16.0
config.frame_width = 9.0

class SuccessiveIncreases(Scene):
    def construct(self):
        # Colors
        C_BASE = GRAY_E
        C_100 = WHITE
        C_30 = BLUE
        C_20 = ORANGE
        C_6 = GREEN
        C_RESULT = YELLOW_B
        
        s_base = 4.0  # Size of the 100% square
        
        # --- INTRO ---
        title = Text("Prices increased by 30%,\nthen by another 20%.", font_size=40, color=WHITE).to_edge(UP, buff=1)
        question = Text("What is the total increase?", font_size=40, color=YELLOW).next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.wait(3.5)
        self.play(FadeIn(question, shift=UP))
        self.wait(1.5)

        # --- WRONG ANSWER: 50%? CROSSED OUT ---
        wrong_answer = Text("50%?", font_size=120, color=WHITE).move_to(ORIGIN)
        self.play(Write(wrong_answer))
        self.play(Indicate(wrong_answer, scale_factor=1.2, color=RED))

        # Red crossing lines
        cross_line1 = Line(wrong_answer.get_corner(DL), wrong_answer.get_corner(UR), color=RED, stroke_width=10)
        cross_line2 = Line(wrong_answer.get_corner(UL), wrong_answer.get_corner(DR), color=RED, stroke_width=10)

        self.play(Create(cross_line1), Create(cross_line2), run_time=0.5)
        self.wait(2)

        self.play(FadeOut(title), FadeOut(question), FadeOut(wrong_answer), FadeOut(cross_line1), FadeOut(cross_line2))

        # --- STEP 1: INITIAL PRICE (100%) ---
        sq_100 = Rectangle(height=s_base, width=s_base, stroke_width=4, stroke_color=C_100)
        label_100 = Text("100%", font_size=60).move_to(sq_100.get_center())
                
        self.play(Create(sq_100))
        self.wait(2.5)
        self.play(Write(label_100))
        self.wait(4.5)

        # --- STEP 2: FIRST INCREASE (+30%) ---
        w_30 = 0.3 * s_base
        sq_30 = Rectangle(
            height=s_base, width=w_30, 
            fill_color=C_30, fill_opacity=0.7, 
            stroke_width=2, stroke_color=C_30
        )
        sq_30.next_to(sq_100, RIGHT, buff=0)
        
        # Tracker for growth progress (0 -> 1)
        growth_30 = ValueTracker(0)
        
        # Redraw lines automatically to stick to the growing rectangle
        v_line = always_redraw(lambda: Line(
            sq_100.get_corner(UR) + RIGHT * growth_30.get_value() * w_30,
            sq_100.get_corner(DR) + RIGHT * growth_30.get_value() * w_30,
            color=C_30, stroke_width=2
        ))
        h_top = always_redraw(lambda: Line(
            sq_100.get_corner(UR),
            sq_100.get_corner(UR) + RIGHT * growth_30.get_value() * w_30,
            color=C_30, stroke_width=2
        ))
        h_bottom = always_redraw(lambda: Line(
            sq_100.get_corner(DR),
            sq_100.get_corner(DR) + RIGHT * growth_30.get_value() * w_30,
            color=C_30, stroke_width=2
        ))
        
        label_30 = MathTex(r"+30\%", font_size=50, color=C_30).next_to(sq_30, DOWN, buff=0.2)
        # 130% label will move to the center of the total width
        label_130 = Text("130%", font_size=60).move_to(sq_100.get_center() + LEFT * w_30/2)
        
        self.add(v_line, h_top, h_bottom)
        self.play(
            sq_100.animate.shift(LEFT * w_30/2),
            Transform(label_100, label_130),
            growth_30.animate.set_value(1),
            label_30.animate.shift(LEFT * w_30/2),
            run_time=2
        )
        sq_30.move_to(VGroup(h_top, h_bottom, v_line).get_center())
        self.add(sq_30)
        self.wait(3)
        self.play(Indicate(label_100, color=YELLOW))
        self.remove(v_line, h_top, h_bottom)
        self.wait(4.5)

        # --- STEP 3: SECOND INCREASE (+20%) ---
        h_20 = 0.2 * s_base
        sq_20_base = Rectangle(
            height=h_20, width=s_base, 
            fill_color=C_20, fill_opacity=0.7, 
            stroke_width=2, stroke_color=C_20
        )
        sq_20_base.next_to(sq_100, UP, buff=0)
        
        sq_20_extra = Rectangle(
            height=h_20, width=w_30, 
            fill_color=C_6, fill_opacity=0.8, 
            stroke_width=2, stroke_color=C_6
        )
        sq_20_extra.next_to(sq_30, UP, buff=0)
        
        # Tracker for vertical growth progress
        growth_20 = ValueTracker(0)
        
        h_line = always_redraw(lambda: Line(
            sq_100.get_corner(UL) + UP * growth_20.get_value() * h_20,
            sq_100.get_corner(UR) + UP * growth_20.get_value() * h_20,
            color=C_20, stroke_width=2
        ))
        v_left = always_redraw(lambda: Line(
            sq_100.get_corner(UL),
            sq_100.get_corner(UL) + UP * growth_20.get_value() * h_20,
            color=C_20, stroke_width=2
        ))
        v_right = always_redraw(lambda: Line(
            sq_100.get_corner(UR),
            sq_100.get_corner(UR) + UP * growth_20.get_value() * h_20,
            color=C_20, stroke_width=2
        ))
        
        label_20 = MathTex(r"+20\%", font_size=50, color=C_20).next_to(sq_20_base, LEFT, buff=0.2).shift(DOWN*0.4)

        # 150% label center after vertical shift
        label_150 = Text("150%", font_size=60).move_to(label_100.get_center() + DOWN * h_20/2)

        label_6 = MathTex(r"6\%", font_size=50, color=C_6).move_to(sq_20_extra.get_center())

        self.add(h_line, v_left, v_right)
        self.play(
            VGroup(sq_100, sq_30).animate.shift(DOWN * h_20/2),
            Transform(label_100, label_150),
            label_30.animate.shift(DOWN * h_20/2),
            growth_20.animate.set_value(1),
            Write(label_20),
            run_time=2
        )
        sq_20_base.move_to(VGroup(v_left, v_right, h_line).get_center())
        self.add(sq_20_base)
        self.remove(h_line, v_left, v_right)
        self.wait(3.5)
        
        sq_20_extra.next_to(sq_30, UP, buff=0)
        label_6 = MathTex(r"6\%", font_size=50, color=C_6).move_to(sq_20_extra.get_center()+UP*0.8+RIGHT * 1)
        
        # 156% label centered on main square
        label_156 = Text("156%", font_size=60).move_to(label_100.get_center())
        
        self.play(
            GrowFromEdge(sq_20_extra, DOWN),
            Transform(label_100, label_156),
            Write(label_6),
            run_time=2
        )
        self.wait(5.5)

        # --- STEP 4: FINAL CALCULATION ---
        all_objects = VGroup(sq_100, sq_30, sq_20_base, sq_20_extra, label_100, label_30, label_20, label_6)
        
        calc_title = Text("Why 56%?", font_size=60, color=YELLOW).to_edge(UP, buff=1.5)
        
        eq1 = MathTex(r"30\%", r" + ", r"20\%", r" + ", r"6\%", r" = ", r"56\%", font_size=80).next_to(calc_title, DOWN, buff=0.5)
        eq1[0].set_color(C_30)
        eq1[2].set_color(C_20)
        eq1[4].set_color(C_6)
        eq1[6].set_color(C_RESULT)

        self.play(
            all_objects.animate.scale(0.8).shift(DOWN * 1),
            Write(calc_title)
        )
        self.wait(1.5)
        
        # Pointing to areas sequentially
        self.play(Indicate(sq_30), Write(eq1[0]))
        self.play(Indicate(sq_20_base), Write(eq1[1:3]))
        self.play(Indicate(sq_20_extra), Write(eq1[3:5]))
        self.wait(3)
        self.play(Write(eq1[5:]))
        self.wait(2)
        self.play(Indicate(eq1[6], scale_factor=1.5))
        self.wait(1.5)

        # --- OUTRO ---
        self.play(FadeOut(all_objects), FadeOut(calc_title), FadeOut(eq1))
        
        # --- STEP 5: QUICK FORMULA ---
        formula_title = Text("The Formula:", font_size=50, color=WHITE).to_edge(UP, buff=1.5)
        
        formula = MathTex(
            "x\%", " + ", "y\%", " + ", "{x \cdot y", "\over", "100}", "\%",
            font_size=90
        ).move_to(ORIGIN)
        
        formula[0].set_color(C_30)  # x
        formula[2].set_color(C_20)  # y
        formula[4:7].set_color(C_6) # x*y/100
        
        self.play(Write(formula_title))
        self.play(Write(formula[0:3])) # x% + y%
        self.wait(2)
        self.play(Write(formula[3:]))  # + x*y/100 %
        
        # Numerical example
        example = MathTex(
            "30\%", " + ", "20\%", " + ", "{30 \cdot 20", "\over", "100}\%", " = 56\%",
            font_size=60, color=GRAY_A
        ).next_to(formula, DOWN, buff=1)
        
        self.play(FadeIn(example, shift=UP))
        self.wait(7.5)
        
        self.play(FadeOut(formula_title), FadeOut(formula), FadeOut(example))
        
        final_text = Text("Mathematics\nis simple!", font_size=90, color=BLUE).move_to(UP * 2)
        sub_text = Text("Follow for new perspectives", font_size=35, color=GRAY).next_to(final_text, DOWN, buff=1)
        self.play(Write(final_text), FadeIn(sub_text, shift=UP))
        self.wait(6.5)
