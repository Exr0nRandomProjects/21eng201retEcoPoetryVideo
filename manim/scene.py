from manim import *

POEM = [
#     \/ xpos
#            \/ y shift
#                  \/ begin timestamp
#                        \/ duration, None = (until next - 0.5)
#                              \/ onscreen length (number of lines remaining to stay onscreen)
#                                  \/ text
# [
#     ( None,  0.5,  1.00, None, 0, "In the beginning," ),
#     ( None,  0.5,  3.00, None, 0, "it was" ),
#     ( None,  0.5,  5.00, None, 0, "chaotic." ),
#     ( None, -0.5,  7.00, None, 0, "A stew" ),
#     ( None, -0.5,  8.00, None, 1, "almost" ),
#     ( None, -0.5,  9.00, None, 0, "conscious." ),
# ],
# [
#     ( None,  0.5,  1.00, None, 0, "Perception," ),
#     ( None,  0.5,  3.00, None, 0, "only of the present." ),
#     ( None, -0.5,  7.00, None, 0, "An ape" ),
#     None,
#     ( None, -0.5,  9.00, None, 0, "human." ),
# ],
#         ]

[ ( None, 0.5 ), [
    (   1.00, None, 1, "In the beginning," ),
    (   3.00, None, 1, "it was" ),
    (   5.00, None, 1, "chaotic." ),
]],
[ ( None, -0.5 ), [
    (   7.00, None, 0, "A stew" ),
    (   8.00, None, 2, "almost", True ),
    (   9.00, None, 0, "conscious." ),
]],
[ ( None, 0.5 ), [
    (   1.00, None, 1, "Perception," ),
    (   3.00, None, 1, "only of the present." ),
]],
[ ( None, -0.5 ), [
    (   7.00, None, 0, "An ape" ),
    None,
    (   9.00, None, 0, "human." ),
]],
]

KEARN_GAP = 0.4
CHAR_HEIGHT = 0.8
COMMA_HEIGHT = 0.12

def is_shifted(s):
    for char in ',;yp':
        if char in s:
            return True
    return False

class textTest(Scene):
    def construct(self):
        onscreen = []
        keyobjs = []

        for keyopt, line in POEM:
            # calculate edge cases
            yoffset = [ int(is_shifted(val[3])) if val is not None else 0 for val in line ]
            keystones = [ i for i,val in enumerate(line) if val is None ]

            # create the base
            if len(keystones) > 0:
            # if len(keyobjs) > 0:
                anims = [ obj[1] for obj in keyobjs ]
                keyobj = anims[0]
            else:
                anims = [Text("e", color=BLUE)]
                keyobj = anims[0]
                keystones = [-1]
                # x shift
                if keyopt[0] is None:
                    keyobj.to_edge(LEFT)
                else:
                    keyobj.shift([KEARN_GAP*keyopt[0], 0, 0])
                # y shift
                if keyopt[1] is not None:
                    anims[0].shift([0, CHAR_HEIGHT*keyopt[1], 0])

            last = False
            if keystones[0] < 0:
                before_key = []
            else:
                before_key = list(zip(line, yoffset))[:keystones[0]]

            after_key  = list(zip(line, yoffset))[keystones[0]+1:]


            print('pre',keyobj)
            for val, toshift in reversed(before_key):
                anims.insert(0, Text(val[3], color=WHITE)
                        .next_to(anims[0], LEFT, buff=KEARN_GAP)
                        .align_to(keyobj, DOWN)
                        .shift([0, -COMMA_HEIGHT*toshift, 0])
                        )
                onscreen.insert(0, [val[2], anims[0]])
                if type(val[-1]) != str:
                    keyobjs.insert(0, anims[0])

            # print(len(anims), keystones[0]+1)
            anims.append(keyobj)
            if keystones[0] < 0: anims.pop(0)

            print('post',keyobj)

            for val, toshift in after_key:
                anims.append(Text(val[3], color=WHITE)
                        .next_to(anims[-1], RIGHT, buff=KEARN_GAP)
                        .align_to(keyobj, DOWN)
                        .shift([0, -COMMA_HEIGHT*toshift, 0])
                        )
                onscreen.append([val[2], anims[-1]])
                if type(val[-1]) != str:
                    keyobjs.append(anims[-1])

            anims.pop(keystones[0]+1)

            # for val, toshift in zip(line, yoffset):
            #     print(val, toshift)
            #     if val is None:
            #         anims.append(keyobj)
            #     else:
            #         anims.append(Text(val[3], color=WHITE)
            #                 .next_to(anims[-1], RIGHT, buff=KEARN_GAP)
            #                 .align_to(keyobj, DOWN)
            #                 .shift([0, -COMMA_HEIGHT*toshift, 0])
            #                 )
            #         onscreen.append([val[2], anims[-1]])
            #         if type(val[-1]) != str:
            #             keyobjs.append(anims[-1])

            for i,anim in enumerate(anims):
                if i in keystones: continue
                self.play(Create(anim))

            self.wait(1)

            for obj in onscreen:
                obj[0] -= 1
            try:
                self.play(*[ FadeOut(obj[1]) for obj in onscreen if obj[0] < 0 ])
            except ValueError:
                pass
            onscreen = [ obj for obj in onscreen if obj[0] >= 0 ]


