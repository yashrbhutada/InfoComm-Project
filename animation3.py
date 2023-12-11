from manim import *

class BoxExample(Scene):
    def construct(self):
        textbox = Text("Total length\nof each\ncodeword")
        textbox.scale(0.6)
        text_box1 = Tex("$l_i,i\in(1.k)$")
        text_box2 = Tex("$\Sigma{l_i}$")
        box = SurroundingRectangle(textbox, buff=0.5)
        box1 = SurroundingRectangle(text_box1, buff=0.5,color=BLUE)
        box2 = SurroundingRectangle(text_box2, buff=0.5,color=GREEN)

        group = VGroup(textbox, box)
        group1 = VGroup(text_box1, box1)
        group2 = VGroup(text_box2, box2)

        arrow = Arrow(
            textbox.get_center()+2*LEFT+1.7*UP,
            (textbox.get_center()+ 2*LEFT+1.7*UP) + 1.5 * RIGHT,
            buff=0.1,
            color=WHITE,
        )

        arrow1 = Arrow(
            text_box1.get_bottom()+RIGHT+1.7*UP,
            (text_box1.get_bottom()+RIGHT+ 1.7*UP) + 3 * DOWN,
            buff=0.1,
            color=WHITE,
        )

        arrow2 = Arrow(
            text_box2.get_corner(UR)+1.7*DOWN,
            text_box2.get_corner(UR)+1.7*DOWN +  RIGHT + UP,
            buff=0.1,
            color=WHITE,
        )

        self.play(Write(group))
        self.wait()
        self.play(ApplyMethod(group.shift, 4.5*LEFT + UP * 2))
        self.play(Write(arrow))

        self.play(Write(group1))
        self.wait()
        self.play(ApplyMethod(group1.shift,RIGHT+UP * 2))

        self.play(Write(group2))
        self.wait()
        self.play(ApplyMethod(group2.shift, RIGHT+DOWN * 2))
        self.play(Write(arrow1))


        text3 = Text("Total Bits").next_to(arrow2, 0.1*RIGHT+UP)
        text3.scale(1)
        self.play(Write(text3))
        self.wait()
        self.play(FadeOut(group,arrow,arrow1,group1,group2,text3))

        textbox = Text("Total\nIntermediate\nvalues")
        textbox.scale(0.6)
        text_box1 = Text("QN")
        text_box2 = Text("QNT")

        box = SurroundingRectangle(textbox, buff=0.5)
        box1 = SurroundingRectangle(text_box1, buff=0.5,color=BLUE)
        box2 = SurroundingRectangle(text_box2, buff=0.5,color=GREEN)

        group = VGroup(textbox, box)
        group1 = VGroup(text_box1, box1)
        group2 = VGroup(text_box2, box2)

        arrow = Arrow(
            textbox.get_center()+2*LEFT+1.7*UP,
            (textbox.get_center()+ 2*LEFT+1.7*UP) + 1.5 * RIGHT,
            buff=0.1,
            color=WHITE,
        )

        arrow1 = Arrow(
            text_box1.get_bottom()+RIGHT+1.7*UP,
            (text_box1.get_bottom()+ RIGHT+1.7*UP) + 3 * DOWN,
            buff=0.1,
            color=WHITE,
        )

        arrow2 = Arrow(
            text_box2.get_corner(UR)+RIGHT+1.7*DOWN,
            text_box2.get_corner(UR)+RIGHT+1.7*DOWN +  RIGHT + UP,
            buff=0.1,
            color=WHITE,
        )

        self.play(Write(group))
        self.wait()
        self.play(ApplyMethod(group.shift, 4.5*LEFT + UP * 2))
        self.play(Write(arrow))

        self.play(Write(group1))
        self.wait()
        self.play(ApplyMethod(group1.shift, RIGHT + UP * 2))

        self.play(Write(group2))
        self.wait()
        self.play(ApplyMethod(group2.shift, RIGHT + DOWN * 2))
        self.play(Write(arrow1))


        text3 = Text("Total Bits").next_to(arrow2, 0.1*RIGHT+UP)
        text3.scale(1)
        self.play(Write(text3))
        self.wait(2)
        self.play(FadeOut(group,arrow,arrow1,group1,group2,text3))

        textbox = Tex("$\Sigma{l_i}$")
        text_box1 = Text("QNT")

        box = SurroundingRectangle(textbox, buff=0.5, color=GREY)
        box1 = SurroundingRectangle(text_box1, buff=0.5,color=GOLD)

        group = VGroup(textbox, box)
        group1 = VGroup(text_box1, box1)
        self.play(ApplyMethod(group.shift, 4.5*LEFT + UP * 2))
        self.play(ApplyMethod(group1.shift, 4.5*RIGHT + UP * 2))

        arrow = Arrow(
            group.get_corner(DR),
            group.get_corner(DR) + 1.5 * RIGHT+1.5*DOWN,
            buff=0.1,
            color=WHITE,
        )

        arrow1 = Arrow(
            group1.get_corner(DL),
            group1.get_corner(DL) + 1.2 * DOWN+1.2*LEFT,
            buff=0.1,
            color=WHITE,
        )

        textnew = Text("Average bits consumed")
        textnew.scale(0.5)

        self.play(Write(arrow))
        self.play(Write(arrow1))
        self.play(Write(textnew))
        self.wait()

        calc = Tex("$\\text{Communication Load} = \\frac{\sum{L_i}}{QNT}$").move_to(DOWN)

        self.play(Write(calc))
        self.wait(2)
        self.play(FadeOut(arrow,arrow1,calc,textnew,group,group1))
