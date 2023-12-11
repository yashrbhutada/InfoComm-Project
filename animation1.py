from manim import *

class BoxExample(Scene):
    def construct(self):
        textbox = Text("Input files")
        textbox.scale(0.6)
        text_box1 = Tex("$(F_{2^{T}})^N$")
        text_box2 = Tex("$F_{2^T}$")
        text_box3 = Tex("$F_{2^B}$")
        
        box = SurroundingRectangle(textbox, buff=0.5)
        box1 = SurroundingRectangle(text_box1, buff=0.5)
        box2 = SurroundingRectangle(text_box2, buff=0.5)
        box3 = SurroundingRectangle(text_box3, buff=0.5)

        group = VGroup(textbox, box)
        group1 = VGroup(text_box1, box1)
        group2 = VGroup(text_box2, box2)
        group3 = VGroup(text_box3, box3)

        arrow = Arrow(
            textbox.get_center()+4*LEFT+1.7*UP,
            (textbox.get_center()+ 4*LEFT+1.7*UP) + 1.5 * RIGHT,
            buff=0.1,
            color=WHITE,
        )

        arrow1 = Arrow(
            text_box1.get_bottom()+LEFT+1.7*UP,
            (text_box1.get_bottom()+ LEFT+1.7*UP) + 3 * DOWN,
            buff=0.1,
            color=WHITE,
        )

        arrow2 = Arrow(
            text_box2.get_corner(UR)+LEFT+1.7*DOWN,
            text_box2.get_corner(UR)+LEFT+1.7*DOWN +  RIGHT + UP,
            buff=0.1,
            color=WHITE,
        )

        arrow3 = Arrow(
            text_box3.get_corner(DR)+LEFT+1.7*UP,
            text_box3.get_corner(DR)+LEFT+1.7*UP + RIGHT+DOWN,
            buff=0.1,
            color=WHITE,
        )

        # Add and shift the first group
        self.play(Write(group))
        self.wait()
        self.play(ApplyMethod(group.shift, 5.5*LEFT + UP * 2))
        self.play(Write(arrow))

        self.play(Write(group1))
        self.wait()
        self.play(ApplyMethod(group1.shift, LEFT + UP * 2))

        # Add and shift the second group
        self.play(Write(group2))
        self.wait()
        self.play(ApplyMethod(group2.shift, LEFT + DOWN * 2))
        self.play(Write(arrow1))

        # Add and shift the third group
        self.play(Write(group3))
        self.wait()
        self.play(ApplyMethod(group3.shift, RIGHT * 1.2))
        self.play(Write(arrow2))
        self.play(Write(arrow3))

        # Add text beside the arrows
        text1 = Text("Map function").next_to(arrow1, LEFT)
        text1.scale(0.6)
        text2 = Text("Reduce").next_to(arrow2, RIGHT)
        text2.scale(0.6)
        text3 = Text("Intermediate values of length T").next_to(text_box2, 1.8*DOWN)
        text3.scale(0.6)
        text4 = Text("Stream of\n bits of\n length B").next_to(text_box3, UP)
        text4.scale(0.6)
        self.play(Write(text1), Write(text2))
        self.play(Write(text3), Write(text4))

        self.wait()










