from manim import * 
from manim_slides import Slide

def add_vectors(a, b):
    return [_a + _b for _a, _b in zip(a, b)]

def middle_point(a, b):
    return [(_a + _b) / 2 for _a, _b in zip(a, b)]

class QueueVisualization(Slide):
    def construct(self):
        start = [2, 0, 0]
        middle = [0, 0, 0]
        end = [-2, 0, 0]
        radius = 0.5

        states = [
            LabeledDot("S1", radius, point=start),
            LabeledDot("S2", radius, point=middle),
            LabeledDot("S3", radius, point=end)
        ]

        arrows = [
            CurvedArrow(add_vectors(start, [0, radius, 0]), add_vectors(middle, [0, radius, 0])),
            CurvedArrow(add_vectors(middle, [0, -1 * radius, 0]), add_vectors(start, [0, -1 * radius, 0])),
            CurvedArrow(add_vectors(middle, [0, radius, 0]), add_vectors(end, [0, radius, 0])),
            CurvedArrow(add_vectors(end, [0, -1 * radius, 0]), add_vectors(middle, [0, -1 * radius, 0]))
        ]

        texts = [
            [Tex(r"$\lambda$", font_size=36), add_vectors(middle_point(start, middle), [0, radius * 2.5, 0])]
        ]

        for text in texts:
            text[0].move_to([0, 5 * radius, 0])

        for state in states:
            self.play(Write(state))
        for arrow in arrows:
            self.play(Write(arrow))
        for text in texts:
            self.play(Write(text[0]))
            self.play(text[0].animate.move_to(text[1]))
        self.wait()
        self.next_slide()
