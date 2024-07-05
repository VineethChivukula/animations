from manim import *


class LinkedListCycle(Scene):
    def construct(self):
        num_nodes = 4  # Number of nodes in the linked list
        square_size = 2  # Size of each square node
        arrow_length = 1.5  # Length of each arrow

        # Starting position for the first node
        start_position = LEFT * 5.3

        nodes = []
        arrows = []

        # Create nodes and arrows
        for i in range(num_nodes):
            # Create a square node
            node = Square(side_length=square_size)
            node.shift(start_position + RIGHT *
                       (i * (square_size + arrow_length)))
            nodes.append(node)

            # Create an arrow if it's not the last node
            if i < num_nodes - 1:
                arrow = Arrow(start=node.get_right(),
                              end=node.get_right() + RIGHT * arrow_length, buff=0.1)
                arrows.append(arrow)

        # Write text on the nodes
        numbers = ["3", "2", "0", "-4"]
        texts = [Text(num).move_to(sq) for num, sq in zip(numbers, nodes)]

        # Add nodes, texts, and arrows to the scene
        self.play(*[Create(node) for node in nodes])
        self.play(*[Create(txt) for txt in texts])
        self.wait(1)
        self.play(*[Create(arrow) for arrow in arrows])
        self.wait(1)

        # Create a cycle arrow from the last node (-4) to the second node (2)
        cycle_arrow = CurvedArrow(
            start_point=nodes[-1].get_top(),
            end_point=nodes[1].get_top(),
            angle=PI / 2,  # Adjust the angle to fit the cycle appropriately
        )

        self.play(Create(cycle_arrow))
        self.wait(1)

        # Create and position "slow", and "fast" texts
        slow = Text("s").next_to(nodes[0], DOWN, buff=0.5)
        fast = Text("f").next_to(nodes[1], DOWN, buff=0.5)
        self.play(Write(slow), Write(fast))
        self.wait(1)

        # Calculate the left and right shift for the nodes
        right = nodes[1].get_center() - nodes[0].get_center()
        left = -right

        # Move "slow" to the right of the first node
        self.play(slow.animate.shift(right, 0.5*LEFT))
        self.wait(0.5)

        # Move "fast" to the right of the second node and third node
        self.play(fast.animate.shift(2*right))
        self.wait(0.5)

        # Move "slow" to the right of the second node
        self.play(slow.animate.shift(right, 1*RIGHT))
        self.wait(0.5)

        # Move "fast" to the second node and then to third node
        self.play(fast.animate.shift(2*left))
        self.play(fast.animate.shift(right))

        # Create and animate "Cycle detected" text in green color
        cycle_text = Text("Cycle detected!", t2c={"Cycle detected!": GREEN}).next_to(
            VGroup(slow, fast), DOWN, buff=0.5).shift(2.2*LEFT)
        self.play(Write(cycle_text))
        self.play(Transform(cycle_text, Text(
            "Cycle detected!").move_to(cycle_text)))
        self.wait(1)

        # Group all elements and fade them out
        group = VGroup(*nodes, *texts, *arrows,
                       cycle_arrow, slow, fast, cycle_text)
        self.play(FadeOut(group))
        self.wait(1)
