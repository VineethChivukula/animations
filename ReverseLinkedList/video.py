from manim import *


class ReverseLinkedList(Scene):
    def construct(self):
        num_nodes = 5  # Number of nodes in the linked list
        square_size = 1  # Size of each square node
        arrow_length = 1.2  # Length of each arrow

        # Starting position for the first node
        start_position = LEFT * 4

        nodes = []
        arrows = []

        # Create nodes and arrows
        for i in range(num_nodes):
            # Create a square node
            node = Square(side_length=square_size)
            node.shift(start_position + RIGHT *
                       (i * (square_size + arrow_length)))
            nodes.append(node)

            # Create an arrow pointing to the next node
            if i < num_nodes:
                arrow = Arrow(start=node.get_right(
                ), end=node.get_right() + RIGHT * arrow_length, buff=0.1)
                arrows.append(arrow)

        # Write text on the nodes
        numbers = ["1", "2", "3", "4", "5"]
        texts = [Text(num).move_to(sq) for num, sq in zip(numbers, nodes)]

        # Add nodes, texts, and arrows to the scene
        self.play(*[Create(node) for node in nodes])
        self.play(*[Create(txt) for txt in texts])
        self.wait(1)
        self.play(*[Create(arrow) for arrow in arrows])
        self.wait(1)

        # create and position "p", "n" and "c" texts
        c = Text("c").next_to(nodes[0], DOWN, buff=0.5).shift(0.25*RIGHT)
        p = Text("p").next_to(c, 2*LEFT, buff=0.5)
        n = Text("n").next_to(p, LEFT, buff=0.5)
        self.play(Write(p), Write(n), Write(c))
        self.wait(1)

        # Calculate the left and right shift for the nodes
        right = nodes[1].get_center() - nodes[0].get_center()
        left = -right

        # Move n to the right
        self.play(n.animate.shift(2*right))
        self.wait(1)

        # change the direction of the arrow 180 degrees to point to the previous node
        self.play(Rotate(arrows[0], angle=PI,
                  about_point=np.array(nodes[0].get_center())))
        self.wait(1)

        # Move p to the right
        self.play(p.animate.shift(0.3*right))
        self.wait(1)

        # Move c to the right
        self.play(c.animate.shift(right))
        self.wait(1)

        # Move n to the right
        self.play(n.animate.shift(right))
        self.wait(1)

        # change the direction of the arrow 180 degrees to point to the previous node
        self.play(Rotate(arrows[1], angle=PI,
                  about_point=np.array(nodes[1].get_center())))
        self.wait(1)

        # Move p to the right
        self.play(p.animate.shift(right))
        self.wait(1)

        # Move c to the right
        self.play(c.animate.shift(right))
        self.wait(1)

        # Move n to the right
        self.play(n.animate.shift(right))
        self.wait(1)

        # change the direction of the arrow 180 degrees to point to the previous node
        self.play(Rotate(arrows[2], angle=PI,
                  about_point=np.array(nodes[2].get_center())))
        self.wait(1)

        # Move p to the right
        self.play(p.animate.shift(right))
        self.wait(1)

        # Move c to the right
        self.play(c.animate.shift(right))
        self.wait(1)

        # Move n to the right
        self.play(n.animate.shift(right))
        self.wait(1)

        # change the direction of the arrow 180 degrees to point to the previous node
        self.play(Rotate(arrows[3], angle=PI,
                  about_point=np.array(nodes[3].get_center())))
        self.wait(1)

        # Move p to the right
        self.play(p.animate.shift(right))
        self.wait(1)

        # Move c to the right
        self.play(c.animate.shift(right))
        self.wait(1)

        # Move n to the right
        self.play(n.animate.shift(0.8*right))
        self.wait(1)

        # change the direction of the arrow 180 degrees to point to the previous node
        self.play(Rotate(arrows[4], angle=PI,
                  about_point=np.array(nodes[4].get_center())))
        self.wait(1)

        # Move p to the right
        self.play(p.animate.shift(1.2*right))
        self.wait(1)

        # Move c to the right
        self.play(c.animate.shift(0.6*right))
        self.wait(1)

        # Create a Group and FadeOut
        self.play(FadeOut(Group(*nodes, *texts, *arrows, p, c, n)))
        self.wait(1)
