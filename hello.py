from manim import *

class HelloScene(Scene):
    def construct(self):
        text = Text("Starting")
        self.play(Write(text))
        self.wait(1)