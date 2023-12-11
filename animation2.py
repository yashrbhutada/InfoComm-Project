from manim import *

class BoxExample(Scene):
    def construct(self):
        textbox = Text("Node (k)")
        textbox.scale(0.6)
        text_box1 = Tex("${M_k}$")
        text_box2 = Tex("$X_k\in{F_{Q^{l_k}}}$")

        box = SurroundingRectangle(textbox, buff=0.5)
        box1 = SurroundingRectangle(text_box1, buff=0.5,color=BLUE)
        box2 = SurroundingRectangle(text_box2, buff=0.5,color=GREEN)

        group = VGroup(textbox, box)
        group1 = VGroup(text_box1, box1)
        group2 = VGroup(text_box2, box2)

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
        self.play(Write(group))
        self.wait()
        self.play(ApplyMethod(group.shift, 5.5*LEFT + UP * 2))
        self.play(Write(arrow))

        self.play(Write(group1))
        self.wait()
        self.play(ApplyMethod(group1.shift, LEFT + UP * 2))

        self.play(Write(group2))
        self.wait()
        self.play(ApplyMethod(group2.shift, LEFT + DOWN * 2))
        self.play(Write(arrow1))


        text1 = Text("Mapping").next_to(arrow, UP)
        text1.scale(0.6)
        text2 = Text("Encoding function").next_to(arrow2, 0.1*LEFT+UP)
        text2.scale(0.6)
        text3 = Tex("${\psi_k}(F_{2^T})^{Q(M_K)} \\rightarrow F_{2^{l_k}}$").next_to(arrow2, 0.1*RIGHT+UP)
        text3.scale(1)
        self.play(Write(text1), Write(text2))
        self.play(Write(text3))
        self.wait()
        newtext = Text("Where lk is the\n length variable for\n each node").move_to(1.5*UP+2.5*RIGHT)
        newtext.scale(0.6)
        self.play(Write(newtext))
        self.wait(2)
