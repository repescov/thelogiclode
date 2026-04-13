from manim import *

# Configuration for VERTICAL 4K format (9:16)
config.pixel_height = 3840
config.pixel_width = 2160
config.frame_height = 16.0
config.frame_width = 9.0

class PercentageSwap(Scene):
    def construct(self):
        # Colors
        C_PRICE = YELLOW
        C_PERCENT = TEAL
        C_EQUALS = WHITE

        # --- SCENE 1: THE TAG ---
        tag = RoundedRectangle(corner_radius=0.5, height=4, width=7, color=WHITE, fill_opacity=0.1).move_to(UP * 4)
        
        # Price Row
        price_val = MathTex("75", font_size=140, color=C_PRICE)
        price_unit = Text(" $", font_size=72, color=C_PRICE)
        price_row = VGroup(price_val, price_unit).arrange(RIGHT, buff=0.1).move_to(tag.get_center() + UP * 0.6)
        
        # Discount Row
        discount_sign = Text("-", font_size=90, color=C_PERCENT)
        discount_val = MathTex("16", font_size=140, color=C_PERCENT)
        perc_sign = MathTex(r"\%", font_size=100, color=C_PERCENT)
        discount_row = VGroup(discount_sign, discount_val, perc_sign).arrange(RIGHT, buff=0.1).move_to(tag.get_center() + DOWN * 0.8)
        
        tag_group = VGroup(tag, price_row, discount_row)

        gear1 = Tex(r"$?$", font_size=120).next_to(tag, DOWN, buff=1)
        
        self.play(Create(tag), Write(price_row), Write(discount_row))
        self.play(Indicate(discount_val), gear1.animate.set_color(RED))
        self.wait(1)
        
        # --- SCENE 2: TRANSFORMATION AND SWAP ---
        # Fixed positions (Slots)
        EQUATION_HEIGHT = 4
        SLOT_1 = LEFT * 3 + UP * EQUATION_HEIGHT    # First number position
        SLOT_2 = LEFT * 1.5 + UP * EQUATION_HEIGHT  # Fixed % position
        SLOT_3 = ORIGIN + UP * EQUATION_HEIGHT      # Fixed "of" position
        SLOT_4 = RIGHT * 2 + UP * EQUATION_HEIGHT   # Second number position

        word_of = Text("of", font_size=80).move_to(SLOT_3)

        self.play(
            FadeOut(tag), FadeOut(price_unit), FadeOut(discount_sign), FadeOut(gear1),
            discount_val.animate.move_to(SLOT_1),
            perc_sign.animate.move_to(SLOT_2),
            price_val.animate.move_to(SLOT_4),
            run_time=1.5
        )
        self.play(Write(word_of))
        self.wait(1)

        # Swap effect (numbers only)
        arc_up = ArcBetweenPoints(discount_val.get_center(), price_val.get_center(), angle=-TAU/3)
        arc_down = ArcBetweenPoints(price_val.get_center(), discount_val.get_center(), angle=-TAU/3)

        self.play(
            MoveAlongPath(discount_val, arc_up),
            MoveAlongPath(price_val, arc_down),
            # perc_sign and word_of stay in place
            run_time=2.5,
            rate_func=smooth
        )
        self.wait(1)
        
        # --- SCENE 3: CALCULATION ---
        formula_group = VGroup(price_val, perc_sign, word_of, discount_val)
        equals_calc = MathTex("=", font_size=120).next_to(formula_group, DOWN, buff=1.0)
        
        three_fourths = MathTex(r"\frac{3}{4}", font_size=160, color=C_PRICE).next_to(equals_calc, DOWN, buff=1.5).shift(LEFT*1.5)
        times = MathTex(r"\times", font_size=100).next_to(three_fourths, RIGHT, buff=0.5)
        sixteen = MathTex("16", font_size=140, color=C_PERCENT).next_to(times, RIGHT, buff=0.5)
        
        calc_group = VGroup(three_fourths, times, sixteen)

        self.play(Write(equals_calc))
        self.play(
            TransformFromCopy(discount_val, sixteen),
            TransformFromCopy(price_val, three_fourths),
            Write(times)
        )
        self.wait(1)

        equals_final = MathTex("=", font_size=120).next_to(calc_group, DOWN, buff=1).shift(LEFT * 0.5)
        result_val = MathTex("12", font_size=180, color=GREEN).next_to(equals_final, RIGHT, buff=0.5)
        
        self.play(Write(equals_final), Write(result_val))
        self.play(Indicate(result_val, scale_factor=1.2))
        self.wait(2)

        # --- SCENE 4: OUTRO ---
        self.play(FadeOut(formula_group, equals_calc, calc_group, equals_final, result_val))
        
        final_text = Text("Mathematics\nis simple!", font_size=90, color=BLUE).center().shift(UP * 2)
        sub_text = Text("Follow for new perspectives", font_size=35, color=GRAY).next_to(final_text, DOWN, buff=1)
        
        self.play(Write(final_text))
        self.play(FadeIn(sub_text, shift=UP))
        self.wait(3)
