from manim import *


class SingleNumber(Scene):
    def construct(self):
        # Create squares and arrange them
        squares = [Square(fill_color=BLACK, fill_opacity=1,
                          stroke_color=WHITE, stroke_width=2) for _ in range(5)]
        group = VGroup(*squares).arrange(RIGHT, buff=0.1)

        # Create text objects for each number and move them to the squares
        numbers = ["4", "1", "2", "1", "2"]
        texts = [Text(num).move_to(sq) for num, sq in zip(numbers, squares)]

        # Animate squares and texts
        self.play(*[Create(sq) for sq in squares], *[Write(txt)
                  for txt in texts])
        self.wait(1)

        # Create and animate "i" text
        i_text = Text("i").next_to(squares[1], DOWN, buff=0.5)
        self.play(Write(i_text))
        self.wait(1)

        # Create and animate "ans = 1" text
        ans = Text("ans = 4").next_to(group, UP, buff=0.5)
        self.play(Write(ans))
        self.wait(1)

        # Move "i" until the end of the array
        self.play(i_text.animate.shift(
            squares[1].get_center() - squares[0].get_center()))
        self.wait(0.5)

        self.play(i_text.animate.shift(
            squares[1].get_center() - squares[0].get_center()))
        self.wait(0.5)

        self.play(i_text.animate.shift(
            squares[1].get_center() - squares[0].get_center()))
        self.wait(0.5)

        # Change ans from "ans = 4" to "ans = 4 ^ 1 ^ 2 ^ 1 ^ 2"
        self.play(Transform(ans, Text(
            "ans = 4 ^ 1 ^ 2 ^ 1 ^ 2").move_to(ans)))
        self.wait(0.5)

        # Highlight 1 and 1 with color transitions
        self.play(Transform(ans, Text(
            "ans = 4 ^ 1 ^ 2 ^ 1 ^ 2", t2c={"1": RED}).move_to(ans)))
        self.wait(1)

        # Highlight 2 and 2 with color transitions
        self.play(Transform(ans, Text(
            "ans = 4 ^ 1 ^ 2 ^ 1 ^ 2", t2c={"2": BLUE}).move_to(ans)))
        self.wait(1)

        # Highlight 4 with color transitions
        self.play(Transform(ans, Text(
            "ans = 4 ^ 1 ^ 2 ^ 1 ^ 2", t2c={"4": GREEN}).move_to(ans)))
        self.wait(1)

        # Change ans from "ans = 4 ^ 1 ^ 2 ^ 1 ^ 2" to "ans = 4"
        self.play(Transform(ans, Text("ans = 4").move_to(ans)))
        self.wait(1)

        # Group all elements and fade them out
        group = VGroup(*squares, *texts, i_text, ans)
        self.play(FadeOut(group))
        self.wait(1)
