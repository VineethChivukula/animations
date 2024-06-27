from manim import *


class MaximumAverageSubarrayI(Scene):
    def construct(self):
        # Create squares and arrange them
        squares = [Square(fill_color=BLACK, fill_opacity=1,
                          stroke_color=WHITE, stroke_width=2) for _ in range(6)]
        group = VGroup(*squares).arrange(RIGHT, buff=0.1)

        # Create text objects for each number and move them to the squares
        numbers = ["1", "12", "-5", "-6", "50", "3"]
        texts = [Text(num).move_to(sq) for num, sq in zip(numbers, squares)]

        # Animate squares and texts
        self.play(*[Create(sq) for sq in squares], *[Write(txt)
                  for txt in texts])
        self.wait(1)

        # Create and position "i" and "j" texts
        i_text = Text("i").next_to(squares[0], DOWN, buff=0.5)
        j_text = Text("j").next_to(squares[0], DOWN, buff=0.5).shift(
            0.5*RIGHT)  # shift 0.5 units to the right
        self.play(Write(i_text), Write(j_text))
        self.wait(1)

        # Create and animate "k = 4" text
        k_text = Text("k = 4").next_to(group, UP, buff=0.5)
        self.play(Write(k_text))
        self.wait(1)

        # Create and animate "sum = 1" text
        window_sum_text = Text("sum = 1").next_to(
            VGroup(i_text, j_text), DOWN, buff=0.5)
        self.play(Write(window_sum_text))
        self.wait(1)

        # Create and animate "maxSum = -∞" text
        max_sum_text = Text(
            "maxSum = -∞").next_to(window_sum_text, RIGHT, buff=0.5).shift(1*RIGHT)
        self.play(Write(max_sum_text))
        self.wait(1)

        # Move "j" text to the next square
        self.play(j_text.animate.shift(
            squares[1].get_center() - squares[0].get_center(), 0.5*LEFT))
        self.wait(0.5)

        # Create and animate "sum = 13" text
        self.play(Transform(window_sum_text, Text(
            "sum = 13").move_to(window_sum_text)))
        self.wait(1)

        # Move "j" text to the next square
        self.play(j_text.animate.shift(
            squares[2].get_center() - squares[1].get_center()))
        self.wait(0.5)

        # Create and animate "sum = 8" text
        self.play(Transform(window_sum_text, Text(
            "sum = 8").move_to(window_sum_text)))
        self.wait(1)

        # Move "j" text to the next square
        self.play(j_text.animate.shift(
            squares[3].get_center() - squares[2].get_center()))
        self.wait(0.5)

        # Create and animate "sum = 2" text
        self.play(Transform(window_sum_text, Text(
            "sum = 2").move_to(window_sum_text)))
        self.wait(1)

        # Create and animate "maxSum = 2" text
        self.play(Transform(max_sum_text, Text(
            "maxSum = 2").move_to(max_sum_text)))
        self.wait(1)

        # Move "i" text to the next square
        self.play(i_text.animate.shift(
            squares[1].get_center() - squares[0].get_center()))
        self.wait(0.5)

        # Create and animate "sum = 1" text
        self.play(Transform(window_sum_text, Text(
            "sum = 1").move_to(window_sum_text)))
        self.wait(1)

        # Move "j" text to the next square
        self.play(j_text.animate.shift(
            squares[4].get_center() - squares[3].get_center()))
        self.wait(0.5)

        # Create and animate "sum = 51" text
        self.play(Transform(window_sum_text, Text(
            "sum = 51").move_to(window_sum_text)))
        self.wait(1)

        # Create and animate "maxSum = 51" text
        self.play(Transform(max_sum_text, Text(
            "maxSum = 51").move_to(max_sum_text)))
        self.wait(1)

        # Move "i" text to the next square
        self.play(i_text.animate.shift(
            squares[2].get_center() - squares[1].get_center()))
        self.wait(0.5)

        # Create and animate "sum = 39" text
        self.play(Transform(window_sum_text, Text(
            "sum = 39").move_to(window_sum_text)))
        self.wait(1)

        # Move "j" text to the next square
        self.play(j_text.animate.shift(
            squares[5].get_center() - squares[4].get_center()))
        self.wait(0.5)

        # Create and animate "sum = 42" text
        self.play(Transform(window_sum_text, Text(
            "sum = 42").move_to(window_sum_text)))
        self.wait(1)

        # Create and animate "maxSum = 51" text to "maxAvg = 12.75"
        self.play(Transform(max_sum_text, Text(
            "maxAvg = 12.75").move_to(max_sum_text)))
        self.wait(1)

        # Create and animate "maxSum = 51" text to "maxAvg = 12.75" with color transitions
        self.play(Transform(max_sum_text, Text(
            "maxAvg = 12.75", t2c={"12.75": GREEN}).move_to(max_sum_text)))
        self.wait(0.5)
        self.play(Transform(max_sum_text, Text(
            "maxAvg = 12.75").move_to(max_sum_text)))
        self.wait(0.5)

        # Group all elements and fade them out
        self.play(FadeOut(VGroup(*squares, *texts, i_text,
                  j_text, k_text, window_sum_text, max_sum_text)))
        self.wait(1)
