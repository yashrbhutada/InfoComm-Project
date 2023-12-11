from manim import *

class BoxExample(Scene):
    def construct(self):
        textbox = Text("  ")
        textbox.scale(0.2)
        text_box1 = Text("  ")
        text_box1.scale(0.2)
        text_box2 = Text("  ")
        text_box2.scale(0.2)
        text_box3 = Text("  ")
        text_box3.scale(0.2)

        box = SurroundingRectangle(textbox, buff=0.5)
        box1 = SurroundingRectangle(text_box1, buff=0.5, color=BLUE)
        box2 = SurroundingRectangle(text_box2, buff=0.5, color=GREEN)
        box3 = SurroundingRectangle(text_box3, buff=0.5, color=GREEN)

        group = VGroup(textbox, box)
        group1 = VGroup(text_box1, box1)
        group2 = VGroup(text_box2, box2)
        group3 = VGroup(text_box3, box3)

        group.next_to(5.5 * LEFT + UP * 2)
        group1.next_to(1.5 * LEFT + UP * 2)
        group2.next_to(1.5 * RIGHT + UP * 2)
        group3.next_to(5.5 * RIGHT + UP * 2)

        brace = Brace(VGroup(group, group1, group2, group3), UP, buff=0.2)
        brace_text = brace.get_text("Map Functions")

        center = ORIGIN
        arrow1 = Arrow(group.get_bottom(),center , color=WHITE)
        arrow2 = Arrow(group1.get_bottom() ,center, color=WHITE)
        arrow3 = Arrow(group2.get_bottom(), center , color=WHITE)
        arrow4 = Arrow(group3.get_bottom(),center, color=WHITE)

        textcen = Text("K nodes").next_to(0.2*DOWN+1.3*LEFT)
        textcen.scale(0.5)

        self.play(Write(group), Write(group1), Write(group2), Write(group3))
        self.play(Write(brace), Write(brace_text))
        self.play(Write(arrow1), Write(arrow2), Write(arrow3), Write(arrow4))
        self.play(Write(textcen))
        self.wait()

        self.play(FadeOut(group), FadeOut(group1), FadeOut(group2), FadeOut(group3), FadeOut(brace), FadeOut(brace_text), FadeOut(arrow4), FadeOut(arrow1), FadeOut(arrow2), FadeOut(arrow3), FadeOut(textcen))

        
        text1 = Text("If r = n,").move_to(3.5*UP)
        text1.scale(0.8)
        math1 = Tex("$n \in {1,2,3,..k}$").move_to(2.7*UP)
        arrow1 = Arrow(math1.get_bottom(),center , color=WHITE)
        textarr = Text("Map\nfunction\ncomputed on").next_to(arrow1)
        textarr.scale(0.8)
        group.next_to(5.5 * LEFT)
        group1.next_to(1.5 * LEFT)
        group2.next_to(1.5 * RIGHT)
        group3.next_to(5.5 * RIGHT)

        brace = Brace(VGroup(group, group1, group2, group3), DOWN, buff=0.2)
        brace_text = brace.get_text("n Nodes")

        textfinal = Tex("$\\text{Computational load} = \\frac{n}{k}$")
        textfinal.move_to(3*DOWN)
        self.play(Write(text1), Write(math1))
        self.play(Write(arrow1))
        self.play(Write(textarr))
        self.play(Write(group), Write(group1), Write(group2), Write(group3))
        self.play(Write(brace), Write(brace_text))
        self.play(Write(textfinal))
        self.wait()

