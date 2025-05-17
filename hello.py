from manim import *

class HelloScene(Scene):
    def construct(self):
        text = Text("Starting")
        self.play(Write(text))
        self.wait(1)


class ConstructBackground(Scene):
    def construct(self):
        self.camera.background_color = "white"
        circle = Circle()
        self.play(Create(circle))
        self.wait(1)


class FourCircles(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        circles = VGroup(*[Circle().set_stroke(color=BLACK).shift(RIGHT * i * 1.5) for i in range(4)])
        self.play(FadeIn(circles))


class AudiLogo(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        circles = VGroup(*[Circle().set_stroke(color=BLACK, width=13).shift(RIGHT * i * 1.5) for i in range(4)])

        fades = [FadeIn(circle, run_time=0.4, rate_func=smooth) for circle in circles]

        audiText = Text("Audi", font="Segoe UI").next_to(circles, DOWN, buff=0.5).set_stroke(color=BLACK, width=3).set_fill(BLACK)

        audiLogo = VGroup(circles, audiText)

        audiLogo.move_to(ORIGIN)

        self.play(LaggedStart(*fades, lag_ratio=0.5))
        self.play(FadeIn(audiText))
        self.wait()
