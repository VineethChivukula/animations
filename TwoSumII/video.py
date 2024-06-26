from manim import *


class TwoSumII(Scene):
    def construct(self):
        # Create squares and arrange them
        squares = [Square(fill_color=BLACK, fill_opacity=1,
                          stroke_color=WHITE, stroke_width=2) for _ in range(4)]
        group = VGroup(*squares).arrange(RIGHT, buff=0.1)

        # Create text objects for each number and move them to the squares
        numbers = ["2", "7", "11", "15"]
        texts = [Text(num).move_to(sq) for num, sq in zip(numbers, squares)]

        # Animate squares and texts
        self.play(*[Create(sq) for sq in squares], *[Write(txt)
                  for txt in texts])
        self.wait(0.5)

        # Create and position "i" and "j" texts
        i_text = Text("i").next_to(squares[0], DOWN, buff=0.5)
        j_text = Text("j").next_to(squares[-1], DOWN, buff=0.5)
        self.play(Write(i_text), Write(j_text))
        self.wait(0.5)

        # Create and animate "target = 18" text
        target_sum_text = Text("target = 18").next_to(group, UP, buff=0.5)
        self.play(Write(target_sum_text))
        self.wait(0.5)

        # Create and animate "currentSum = nums[i] + nums[j]" text
        current_sum_text = Text(
            "currentSum = nums[i] + nums[j]").next_to(VGroup(i_text, j_text), DOWN, buff=0.5)
        self.play(Write(current_sum_text))
        self.wait(0.5)

        # Create and animate "currentSum = 17" with color transitions
        self.play(Transform(current_sum_text, Text(
            "currentSum = 17").move_to(current_sum_text)))
        self.wait(0.5)
        self.play(Transform(current_sum_text, Text(
            "currentSum = 17", t2c={"17": RED}).move_to(current_sum_text)))
        self.wait(0.5)
        self.play(Transform(current_sum_text, Text(
            "currentSum = 17").move_to(current_sum_text)))
        self.wait(0.5)

        # Move "i" text to the next square
        self.play(i_text.animate.shift(
            squares[1].get_center() - squares[0].get_center()))
        self.wait(0.5)

        # Create and animate "currentSum = 22" with color transitions
        self.play(Transform(current_sum_text, Text(
            "currentSum = 22").move_to(current_sum_text)))
        self.wait(0.5)
        self.play(Transform(current_sum_text, Text(
            "currentSum = 22", t2c={"22": BLUE}).move_to(current_sum_text)))
        self.wait(0.5)
        self.play(Transform(current_sum_text, Text(
            "currentSum = 22").move_to(current_sum_text)))
        self.wait(0.5)

        # Move "j" text to the previous square
        self.play(j_text.animate.shift(
            squares[2].get_center() - squares[3].get_center()))
        self.wait(0.5)

        # Create and animate "currentSum = 18" with color transitions
        self.play(Transform(current_sum_text, Text(
            "currentSum = 18").move_to(current_sum_text)))
        self.wait(0.5)
        self.play(Transform(current_sum_text, Text("currentSum = 18",
                  t2c={"18": GREEN}).move_to(current_sum_text)))
        self.wait(0.5)
        self.play(Transform(current_sum_text, Text(
            "currentSum = 18").move_to(current_sum_text)))
        self.wait(0.5)

        # Group all elements and fade them out
        all_elements = VGroup(group, i_text, j_text,
                              target_sum_text, current_sum_text, *texts)
        self.play(FadeOut(all_elements))
        self.wait(0.5)
