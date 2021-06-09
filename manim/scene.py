from manim import *

POEM = [
#       \/ begin timestamp
#             \/ duration, None = (until next - 0.5)
#                   \/ onscreen length (number of lines remaining to stay onscreen)
#                       \/ text
[ ( None, 0.5 ), [
    (   1.00, None, 1, "In the beginning," ),
    (   3.00, None, 1, " it was" ),
    (   5.00, None, 1, " chaotic." ),
]],
[ ( None, -0.5 ), [
    (   7.00, None, 0, "A stew" ),
    (   8.00, None, 4, " almost", True ),
    (   9.00, None, 0, " conscious." ),
]],
[ ( None, 0.5 ), [
    (   11.50, None, 1, "Perception," ),
    (   13.00, None, 1, " only of the present." ),
]],
[ ( None, -0.5 ), [
    (   16.00, None, 0, "An ape " ),
    None,
    (   18.00, None, 0, " human." ),
]],
[ ( None, 0.5 ), [
    (  19.50, None, 1, "But from the shifting nature came" ),
]],
[ ( None, -0.5 ), [
    (   24.00, None, 0, "A mind " ),
    None,
    (   27.00, None, 0, " dauntless." ),
]],
]

KEARN_GAP = 0.1
CHAR_WIDTH = 0.4
CHAR_HEIGHT = 0.8
COMMA_HEIGHT = 0.12

def is_shifted(s):
    for char in ',;yqpjg':
        if char in s:
            return True
    return False

def default_dura(s):
    return len(s)/6

class textTest(Scene):
    def construct(self):
        onscreen = []
        keyobjs = []
        tot_dura = 0

        for keyopt, line in POEM:
            # calculate edge cases
            yoffset = [ int(is_shifted(val[3])) if val is not None else 0 for val in line ]
            keystones = [ i for i,val in enumerate(line) if val is None ]

            # create the base
            if len(keystones) > 0:
                anims = [ obj for obj in keyobjs ]
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

            print(before_key, after_key)

            durations = []
            start_times = []

            # construct
            for val, toshift in reversed(before_key):
                anims.insert(0, Text(val[3], color=WHITE)
                        .next_to(anims[0], LEFT, buff=CHAR_WIDTH if val[3][-1] == " " else KEARN_GAP)
                        .align_to(keyobj, DOWN)
                        .shift([0, -COMMA_HEIGHT*toshift, 0]))
                durations.append(val[1] or default_dura(val[3]))
                start_times.append(val[0])
                onscreen.insert(0, [val[2], anims[0]])
                if type(val[-1]) != str:
                    keyobjs.insert(0, anims[0])

            print('anims', anims)

            for val, toshift in after_key:
                anims.append(Text(val[3], color=WHITE)
                        .next_to(anims[-1], RIGHT, buff=CHAR_WIDTH if val[3][0] == " " else KEARN_GAP)
                        .align_to(keyobj, DOWN)
                        .shift([0, -COMMA_HEIGHT*toshift, 0])
                        )
                durations.append(val[1] or default_dura(val[3]))
                start_times.append(val[0])
                onscreen.append([val[2], anims[-1]])
                if type(val[-1]) != str:
                    keyobjs.append(anims[-1])

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
        print('TOTAL DURATION:', tot_dura)

