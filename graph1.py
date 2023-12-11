from manim import *

class Graph2(Scene):
    def construct(self):
        axes = Axes(
            y_range=[0, 1, 0.1],
            x_range=[1, 11, 1]
        )
        axes.add_coordinates()

        graph1 = axes.plot(lambda x: 1 - x / 10,
                           x_range=[1, 10],
                           color=RED)

        graph2 = axes.plot(lambda x: (1 - x / 10) / x,
                           x_range=[1, 10],
                           color=BLUE)

        self.play(Write(axes))
        self.wait(1)

        points = [(2, 0.4), (2, 0.8), (6, 0.0666667), (6, 0.4)]

        dots = VGroup()
        labels = VGroup()

        for x, y in points:
            dot = Dot(axes.coords_to_point(x, y))
            label = Text(f"({x}, {y})", font_size=16)
            label.next_to(dot, UP)
            dot_label = VGroup(dot, label)
            dots.add(dot_label)

        lines = []
        for i in range(len(dots) - 1):
            if i == 0:
                line = DashedLine(dots[i].get_center(), dots[i + 1].get_center())
                label = Text("x2", font_size=18)
                label.next_to(line, RIGHT)
                dashed_line_label = VGroup(line, label)
                lines.append(dashed_line_label)
                labels.add(dashed_line_label)

            if i == 2:
                line = DashedLine(dots[i].get_center(), dots[i + 1].get_center())
                label = Text("x6", font_size=18)
                label.next_to(line, RIGHT)
                dashed_line_label = VGroup(line, label)
                lines.append(dashed_line_label)
                labels.add(dashed_line_label)

        x_label = axes.get_x_axis_label("Computational Load (r)")
        y_label = axes.get_y_axis_label("Communicational Load (L)")

        self.play(
            Write(graph1),
            Write(graph2),
            Write(x_label),
            Write(y_label),
        )

        self.play(*[Create(dot_label) for dot_label in dots])
        self.play(*[Create(line) for line in lines])
        self.play(*[Write(label[1]) for label in labels])

        equation1 = MathTex("\\frac{1}{r} \cdot (1 - \\frac{r}{K})", font_size=25)
        equation1.next_to(labels, DOWN, buff=0.5)
        equation2 = MathTex("1 - \\frac{r}{K}", font_size=25)
        equation2.next_to(labels, DOWN, buff = 0.5)

        legend = VGroup(
            Dot(color=RED),
            equation2,
            Dot(color=BLUE),
            equation1
        )
        legend.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        legend.to_corner(UR)

        self.play(Create(legend))

        self.wait(2)






