from manim import *

class textTest(Scene):
    def construct(self):
        text = Text("Hello there", color=WHITE).to_edge(LEFT)
        text2 = Text("world", color=WHITE).next_to(text, RIGHT)

        self.play(Create(text))
        self.play(Create(text2))

