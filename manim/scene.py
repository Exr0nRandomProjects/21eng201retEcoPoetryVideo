from manim import *

class textTest(Scene):
    def construct(self):
        texts = [ "Hello there", "world,", "my name." ]
        gap = 0.4
        comma_height = 0.12

        yoffset = [ int("," in val or ";" in val) for val in texts ]
        anims = [Text("e", color=BLACK).to_edge(LEFT)]
        for val, toshift in zip(texts, yoffset):
            anims.append(Text(val, color=WHITE)
                    .next_to(anims[-1], RIGHT, buff=gap)
                    .align_to(anims[-1], DOWN)
                    .shift([0, -comma_height*toshift, 0]))

        for anim in anims:
            self.play(Create(anim))

        # text = Text("Hello there", color=WHITE).to_edge(LEFT).set_y(0)
        # text2 = Text("world,", color=WHITE).next_to(text, RIGHT, buff=gap).set_y(0)
        # text3 = Text("my name.", color=WHITE).next_to(text2, RIGHT, buff=gap).set_y(0)
        #
        # self.play(Create(text))
        # self.play(Create(text2))
        # self.play(Create(text3))

