from manim import *

POEM = [
#     \/ xpos
#            \/ y shift
#                  \/ begin timestamp
#                        \/ duration, None = (until next - 0.5)
#                              \/ onscreen length (number of lines remaining to stay onscreen)
#                                  \/ text
[
    ( None,  0.5,  1.00, None, 0, "In the beginning," ),
    ( None,  0.5,  3.00, None, 0, "it was" ),
    ( None,  0.5,  5.00, None, 0, "chaotic." ),
    ( None, -0.5,  7.00, None, 0, "A stew" ),
    ( None, -0.5,  8.00, None, 1, "almost" ),
    ( None, -0.5,  9.00, None, 0, "conscious." ),
],
[
    ( None,  0.5,  1.00, None, 0, "Perception," ),
    ( None,  0.5,  3.00, None, 0, "only of the present." ),
    ( None, -0.5,  7.00, None, 0, "An ape" ),
    None,
    ( None, -0.5,  9.00, None, 0, "human." ),
],
        ]

KEARN_GAP = 0.4
COMMA_HEIGHT = 0.12

class textTest(Scene):
    def construct(self):
        onscreen = []

        for line in POEM:
            # calculate edge cases
            yoffset = [ int("," in val or ";" in val) for val in line if val is not None ]
            keystones = [ i for i,val in enumerate(line) if val is None ]
            print(keystones)

            # create the base
            if len(onscreen) > 0:
                anims = [ obj[1] for obj in onscreen ]
            else:
                anims = [Text("e", color=BLACK)]
            anims[0].to_edge(LEFT)

            for val, toshift in zip(line, yoffset):
                if val is None: continue
                anims.append(Text(val[-1], color=WHITE)
                        .next_to(anims[-1], RIGHT, buff=KEARN_GAP)
                        .align_to(anims[-1], DOWN)
                        .shift([0, -COMMA_HEIGHT*toshift, 0]))

                onscreen.append([val[-2], anims[-1]])

            for anim in anims:
                self.play(Create(anim))

            for obj in onscreen:
                obj[0] -= 1
            self.play(*[ FadeOut(obj[1]) for obj in onscreen if obj[0] < 0 ])
            onscreen = [ obj for obj in onscreen if obj[0] >= 0 ]


