from manim import *

POEM = [
#       \/ begin timestamp
#             \/ duration, None = (until next - 0.5)
#                   \/ onscreen length (number of lines remaining to stay onscreen)
#                       \/ text
# [ ( None, 0.5 ), [
#     (   0.00  +16/60, None, 1, "In the beginning," ),
#     (   1.00  +16/60, None, 1, " it was" ),
#     (   1.00  +47/60, None, 1, " chaotic." ),
# ]],
# [ ( None, -0.5 ), [
#     (   2.00  +42/60, None, 0, "A stew" ),
#     (   8.00  +16/60, None, 4, " almost", True ),
#     (   9.00  +16/60, None, 0, " conscious." ),
# ]],
# [ ( None, 0.5 ), [
#     (   11.50  +16/60, None, 1, "Perception," ),
#     (   13.00  +16/60, None, 1, " only of the present." ),
# ]],
# [ ( None, -0.5 ), [
#     (   16.00  +16/60, None, 0, "An ape " ),
#     None,
#     (   18.00  +16/60, None, 0, " human." ),
# ]],
# [ ( None, 0.5 ), [
#     (  19.50  +16/60, None, 1, "But from the shifting nature came" ),
# ]],
# [ ( None, -0.5 ), [
#     (   24.00  +16/60, None, 0, "A mind " ),
#     None,
#     (   27.00  +16/60, None, 0, " dauntless." ),
# ]],
# [ ( None, 0.5 ), [
#     (   0.00  +16/60, None, 1, "Until finally, we escaped" ),
# ]],
# [ ( None, -0.5 ), [
#     (   0.00  +16/60, None, 0, "the intellectual shade:" ),
# ]],
# [ ( None, 0 ), [
#     (   0.00  +16/60, None, 0, "we became nature's renegades." ),
# ]],


# [ ( None, 0.5 ), [
#     (   0.00  +16/60, None, 1, "When we gained maturity," ),
# ]],
# [ ( None, -0.5 ), [
#     (   0.00  +16/60, None, 0, "we sought security." ),
# ]],
#
# [ ( None, 0.5 ), [
#     (   0.00  +16/60, None, 1, "We harnessed oxen," ),
# ]],
# [ ( None, -0.5 ), [
#     (   0.00  +16/60, None, 0, "and cultivated the land." ),
# ]],
#
# [ ( None, 0.5 ), [
#     (   0.00  +16/60, None, 1, "A potent concotion," ),
# ]],
# [ ( None, -0.5 ), [
#     (   0.00  +16/60, None, 0, "a force none could withstand." ),
# ]],
#
# # [ ( -14, 0.7 ), [
# #     (   0.00  +16/60, None, 2, "And yet" ),
# # ]],
# # [ ( -4, 0 ), [
# #     (   0.00  +16/60, None, 1, "we said" ),
# # ]],
# # [ ( 7, -0.7 ), [
# #     (   0.00  +16/60, None, 0, '"almost."' ),
# # ]],
# [ ( -4, 0.8 ), [
#     (   0.00  +16/60, None, 2, "And yet" ),
# ]],
# [ ( -4, 0 ), [
#     (   0.00  +16/60, None, 1, "we said" ),
# ]],
# [ ( -4, -0.8 ), [
#     (   0.00  +16/60,  0.1, 0, '"'),
#     (   0.00  +16/60, None, 1, 'almost', True),
#     (   0.00  +16/60,  0.1, 0, '"'),
# ]],
# [ ( None, -0.8 ), [
#     (   0.00  +16/60, None, 0, '"We are ' ),
#     None,
#     (   0.00  +16/60, None, 0, ' safe."' ),
# ]],
#
# [ ( 16-20, 0.8 ), [
#     (   0.00  +16/60, None, 2, "We created gunpowder," ),
# ]],
# [ ( 16-33.4, 0 ), [
#     (   0.00  +16/60, None, 1, "Trampled each beast and each flower." ),
# ]],
# [ ( 16-30.7, -0.8 ), [
#     (   0.00  +16/60, None, 0, "Nature did not have the willpower." ),
# ]],
#
# [ ( None, 0 ), [
#     (   0.00  +16/60, None, 0, "We were safe." ),
# ]],
# [ ( None, 0 ), [
#     (   0.00  +16/60, None, 0, "We did it right." ),
# ]],
# [ ( None, 0 ), [
#     (   0.00  +16/60, None, 1, "But in the height" ),
# ]],
# [ ( -12.6, -0.8 ), [
#     (   0.00  +16/60, None, 0, "of our light" ),
#     (   0.00  +16/60, None, 0, " we realized:" ),
# ]],
# [ ( None, 0 ), [
#     (   0.00  +16/60, None, 0, "We were not satisfied." ),
# ]],


# [ ( None, 0.5 ), [
#     (   0.00  +16/60, None, 1, "When we gained security," ),
# ]],
# [ ( None, -0.5 ), [
#     (   0.00  +16/60, None, 0, "we sought prosperity." ),
# ]],
#
# [ ( None, 0.5 ), [
#     (   0.00  +16/60, None, 1, "We invented machines," ),
# ]],
# [ ( None, -0.5 ), [
#     (   0.00  +16/60, None, 0, "and harnessed the lightning." ),
# ]],
#
# [ ( None, 0.5 ), [
#     (   0.00  +16/60, None, 1, "We created vaccines," ),
# ]],
# [ ( None, -0.5 ), [
#     (   0.00  +16/60, None, 0, "and used bleach for whitening." ),
# ]],
#
# [ ( -4, 0.8 ), [
#     (   0.00  +16/60, None, 2, "And yet" ),
# ]],
# [ ( -4, 0 ), [
#     (   0.00  +16/60, None, 1, "we said" ),
# ]],
# [ ( -4, -0.8 ), [
#     (   0.00  +16/60,  0.1, 0, '"'),
#     (   0.00  +16/60, None, 1, 'almost', True),
#     (   0.00  +16/60,  0.1, 0, '"'),
# ]],
# [ ( None, -0.8 ), [
#     (   0.00  +16/60, None, 0, '"We are ' ),
#     None,
#     (   0.00  +16/60, None, 0, ' snug."' ),
# ]],
#
# [ ( -3.8, 0.8 ), [
#     (   0.00  +16/60, None, 2, "We built ivory towers," ),
# ]],
# [ ( -4.65, 0 ), [
#     (   0.00  +16/60, None, 1, "counted kilowatt hours." ),
# ]],
# [ ( 15-30.7, -0.8 ), [
#     (   0.00  +16/60, None, 0, "Nature did not have the willpower." ),
# ]],
#
# [ ( None, 0 ), [
#     (   0.00  +16/60, None, 0, "We were snug." ),
# ]],
# [ ( None, 0 ), [
#     (   0.00  +16/60, None, 0, "We did it right." ),
# ]],
# [ ( None, 0 ), [
#     (   0.00  +16/60, None, 1, "But in the height" ),
# ]],
# [ ( -12.6, -0.8 ), [
#     (   0.00  +16/60, None, 0, "of our light" ),
#     (   0.00  +16/60, None, 0, " we realized:" ),
# ]],
# [ ( None, 0 ), [
#     (   0.00  +16/60, None, 0, "We were not satisfied." ),
# ]],


# [ ( None, 0.5 ), [
#     (   0.00  +16/60, None, 1, "When we gained prosperity," ),
# ]],
# [ ( None, -0.5 ), [
#     (   0.00  +16/60, None, 0, "we fought insecurity." ),
# ]],
#
# [ ( None, 0.5 ), [
#     (   0.00  +16/60, None, 1, "We wrote deuteronomy," ),
# ]],
# [ ( None, -0.5 ), [
#     (   0.00  +16/60, None, 0, "managed the economy." ),
# ]],
#
# [ ( None, 0.5 ), [
#     (   0.00  +16/60, None, 1, "endlessly updated" ),
# ]],
# [ ( None, -0.5 ), [
#     (   0.00  +16/60, None, 0, "our taxonomy of anomalies." ),
# ]],
#
# [ ( -4, 0.8 ), [
#     (   0.00  +16/60, None, 2, "And yet" ),
# ]],
# [ ( -4, 0 ), [
#     (   0.00  +16/60, None, 1, "we said" ),
# ]],
# [ ( -4, -0.8 ), [
#     (   0.00  +16/60,  0.1, 0, '"'),
#     (   0.00  +16/60, None, 1, 'almost', True),
#     (   0.00  +16/60,  0.1, 0, '"'),
# ]],
# [ ( None, -0.8 ), [
#     (   0.00  +16/60, None, 0, '"We are ' ),
#     None,
#     (   0.00  +16/60, None, 0, ' happy."' ),
# ]],

[ ( -3, 0.8 ), [
    (   0.00  +16/60, None, 3, "We sat in rush hour," ),
]],
[ ( -5.65, 0 ), [
    (   0.00  +16/60, None, 2, "ignored meteor showers." ),
]],
[ ( None, -0.8 ), [
    (   0.00  +16/60, None, 3, "We", True ),
]],
[ ( 15-24.05, -0.8 ), [
    (   0.00  +16/60, None, 0, "did not have the willpower." ),
]],

[ ( None, 0 ), [
    None,
    (   0.00  +16/60, None, 0, " were snug." ),
]],
[ ( None, 0 ), [
    None,
    (   0.00  +16/60, None, 0, " did it right." ),
]],
[ ( None, 0 ), [
    (   0.00  +16/60, None, 1, "But in the height" ),
]],
[ ( -12.6, -0.8 ), [
    (   0.00  +16/60, None, 0, "of our light" ),
    (   0.00  +16/60, None, 0, " we realized:" ),
]],
[ ( None, 0 ), [
    (   0.00  +16/60, None, 1, "We are the parasite." ),
]],
]

KEARN_GAP = 0.1
CHAR_WIDTH = 0.4
CHAR_HEIGHT = 0.8
COMMA_HEIGHT = 0.12
QUOTE_HEIGHT = 0.3

def is_shifted(s):
    for char in ',;yqpjg':
        if char in s:
            return -COMMA_HEIGHT
    if len(s) == 1 and s in '"\'':
        return QUOTE_HEIGHT
    return 0

def default_dura(s):
    return len(s)/26

class textTest(Scene):
    def construct(self):
        onscreen = []
        keyobjs = []
        tot_dura = 0

        for keyopt, line in POEM:
            # calculate edge cases
            yoffset = [ is_shifted(val[3]) if val is not None else 0 for val in line ]
            keystones = [ i for i,val in enumerate(line) if val is None ]

            # create the base
            if len(keystones) > 0:
                anims = [ obj[1] for obj in keyobjs ]
                keyobj = anims[0]
            else:
                anims = [Text("e", color=BLUE)]
                keyobj = anims[0]
                keystones = [-1]
                # x shift
                if keyopt[0] is None:
                    keyobj.to_edge(LEFT).shift([-CHAR_WIDTH, 0, 0])
                else:
                    keyobj.shift([CHAR_WIDTH*keyopt[0], 0, 0])
                # y shift
                if keyopt[1] is not None:
                    anims[0].shift([0, CHAR_HEIGHT*keyopt[1], 0])

            # partition
            if keystones[0] < 0:
                before_key = []
            else:
                before_key = list(zip(line, yoffset))[:keystones[0]]
            after_key  = list(zip(line, yoffset))[keystones[0]+1:]

            durations = []
            start_times = []

            # construct
            for val, toshift in reversed(before_key):
                anims.insert(0, Text(val[3], color=WHITE)
                        .next_to(anims[0], LEFT, buff=CHAR_WIDTH if val[3][-1] == " " else KEARN_GAP)
                        .align_to(keyobj, DOWN)
                        .shift([0, toshift, 0]))
                durations.append(val[1] or default_dura(val[3]))
                start_times.append(val[0])
                onscreen.insert(0, [val[2], anims[0]])
                if type(val[-1]) != str:
                    keyobjs.insert(0, [val[2], anims[0]])

            print('anims', anims)

            for val, toshift in after_key:
                anims.append(Text(val[3], color=WHITE)
                        .next_to(anims[-1], RIGHT, buff=CHAR_WIDTH if val[3][0] == " " else KEARN_GAP)
                        .align_to(keyobj, DOWN)
                        .shift([0, toshift, 0])
                        )
                durations.append(val[1] or default_dura(val[3]))
                start_times.append(val[0])
                onscreen.append([val[2], anims[-1]])
                if type(val[-1]) != str:
                    keyobjs.append([val[2], anims[-1]])

            sub = 0
            for i,anim in enumerate(anims[1 if keystones[0] < 0 else 0:]):
                if i in keystones:
                    sub += 1
                    continue
                to_wait = max(start_times[i-sub]-tot_dura, 0)
                self.wait(to_wait)
                tot_dura += to_wait

                self.play(Write(anim, run_time=durations[i-sub]))
                # self.play(Write(anim, run_time=2))
                tot_dura += durations[i-sub]

            # draw
            for obj in onscreen:
                obj[0] -= 1
            try:
                to_rem = [ FadeOut(obj[1]) for obj in onscreen if obj[0] < 0 ]
                self.play(*to_rem)
                self.remove(*to_rem)
                tot_dura += 1
            except ValueError:
                pass
            onscreen = [ obj for obj in onscreen if obj[0] >= 0 ]

            # also remove things from keyobjs, this is sooo undry
            for obj in keyobjs:
                obj[0] -= 1
            keyobjs = [ obj for obj in keyobjs if obj[0] >= 0 ]

        print(onscreen)
        print('TOTAL DURATION:', tot_dura)

        self.wait(3)
        self.play(*[FadeOut(obj[1]) for obj in onscreen], run_time = 6)
        self.wait(2)

