from manim import *


class BinarySearch(Scene):
    def construct(self):
        # Create squares and arrange them
        squares = [Square(fill_color=BLACK, fill_opacity=1,
                          stroke_color=WHITE, stroke_width=2) for _ in range(6)]
        group = VGroup(*squares).arrange(RIGHT, buff=0.1)

        # Create text objects for each number and move them to the squares
        numbers = ["-1", "0", "3", "5", "9", "12"]
        texts = [Text(num).move_to(sq) for num, sq in zip(numbers, squares)]

        # Animate squares and texts
        self.play(*[Create(sq) for sq in squares], *[Write(txt)
                  for txt in texts])
        self.wait(1)

        # Create and position "low", "mid", and "high" texts
        low = Text("l").next_to(squares[0], DOWN, buff=0.5)
        mid = Text("m").next_to(squares[2], DOWN, buff=0.5)
        high = Text("h").next_to(squares[-1], DOWN, buff=0.5)
        self.play(Write(low), Write(mid), Write(high))
        self.wait(1)

        # Create and animate "target = 5" text
        target = Text("target = 5").next_to(group, UP, buff=0.5)
        self.play(Write(target))
        self.wait(1)

        # Create and animate "nums[m] < target" text
        condition_text = Text("nums[m] < target").next_to(
            VGroup(low, mid, high), DOWN, buff=0.5)
        self.play(Write(condition_text))
        self.wait(1)

        # Create and animate "nums[m] < target" with color transitions
        self.play(Transform(condition_text, Text("nums[m] < target", t2c={
            "target": RED}).move_to(condition_text)))
        self.wait(1)
        self.play(Transform(condition_text, Text(
            "nums[m] < target").move_to(condition_text)))
        self.wait(1)

        # Move "low" text to the right of "m" square
        self.play(low.animate.shift(
            squares[3].get_center() - squares[0].get_center(), 0.5*LEFT))
        self.wait(0.5)

        # Move "m" text to the right of "l" square
        self.play(mid.animate.shift(
            squares[2].get_center() - squares[0].get_center()))
        self.wait(0.5)

        # Create and animate "nums[m] > target" with color transitions
        self.play(Transform(condition_text, Text("nums[m] > target", t2c={
            "target": BLUE}).move_to(condition_text)))
        self.wait(1)
        self.play(Transform(condition_text, Text(
            "nums[m] > target").move_to(condition_text)))
        self.wait(1)

        # Move "high" text to the left of "m" square
        self.play(high.animate.shift(
            squares[3].get_center() - squares[-1].get_center(), 0.5*RIGHT))
        self.wait(0.5)

        # Move "m" text to "l" square
        self.play(mid.animate.shift(
            squares[0].get_center() - squares[1].get_center()))
        self.wait(0.5)

        # Create and animate "nums[m] == target" with color transitions
        self.play(Transform(condition_text, Text("nums[m] == target", t2c={
            "target": GREEN}).move_to(condition_text)))
        self.wait(1)
        self.play(Transform(condition_text, Text(
            "nums[m] == target").move_to(condition_text)))
        self.wait(1)

        # Group all elements and fade them out
        self.play(FadeOut(VGroup(*squares, *texts, low,
                  mid, high, target, condition_text)))
        self.wait(1)
