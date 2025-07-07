from manim import * 
from manim.utils.color.X11 import BLUE2
import numpy as np
from manim_slides import Slide

def middle_point(a, b):
    return (a + b) / 2

ORIGIN = np.array([0, 0, 0])
STATE_RADIUS = 0.5
LABEL_ORIGIN = np.array([0.0, float(5 * STATE_RADIUS), 0.0])

class State:
    def __init__(self, label: str, definition: str) -> None:
        self.label = label
        self.position = ORIGIN
        self.connected_edges = []
        self.definition = definition
    
    def move_to(self, position):
        self.position = position

    def render(self, slide: Slide):
        label = Tex('$' + self.label.replace('$', '') + r' \equiv ' + self.definition + '$', font_size=36)
        label.move_to(LABEL_ORIGIN)
        slide.play(Write(label))
        slide.play(FadeOut(label))
        self.rendered = LabeledDot(self.label, STATE_RADIUS, point=self.position)
        slide.play(Write(
            self.rendered
        ))

    def unfocus(self):
        return [
            self.rendered[0].animate.set_color(GREY),
            self.rendered[1].animate.set_color(BLACK)
        ]

    def focus(self):
        return [
            self.rendered[0].animate.set_color(WHITE),
            self.rendered[1].animate.set_color(BLACK)
        ]

class Edge:
    def __init__(self, origin, dest, label) -> None:
        self.origin = origin
        self.dest = dest
        self.label = label
        self.direction = 1 if self.origin.position[0] > self.dest.position[0] else -1

    def render(self, slide):
        direction = self.direction
        self.rendered_arrow = CurvedArrow(
            self.origin.position + np.array([0, STATE_RADIUS * direction, 0]),
            self.dest.position + np.array([0, STATE_RADIUS * direction, 0])
        )

        slide.play(Write(self.rendered_arrow))
        self.rendered_label = Tex(self.label, font_size=36)
        label_offset = (self.rendered_arrow.height * 1.5 + STATE_RADIUS) * direction
        label_position = middle_point(self.origin.position, self.dest.position) + np.array([0, label_offset, 0])
        self.rendered_label.move_to(LABEL_ORIGIN * direction)
        slide.play(Write(self.rendered_label))
        slide.play(self.rendered_label.animate.move_to(label_position))

    def focus(self, target: State):
        return [
            self.rendered_label.animate.set_color(
                BLUE if self.origin == target else RED
            ),
            self.rendered_arrow.animate.set_color(
                BLUE if self.origin == target else RED
            )
        ]

    def unfocus(self):
        return [
            self.rendered_label.animate.set_color(GREY),
            self.rendered_arrow.animate.set_color(GREY)
        ]

class Queue:
    def __init__(self, position, canvas_dimensions) -> None:
        self.states = []
        self.edges = []
        self.rendered_states = []
        self.rendered_edges = []
        self.dimensions = canvas_dimensions
        self.position = position

    def add_state(self, label: str, definition: str):
        state = State(label, definition)
        self.states.append(state)

    def add_edge(self, origin_idx, dest_idx, label):
        edge = Edge(self.states[origin_idx], self.states[dest_idx], label)
        self.edges.append(edge)

    def focus_state(self, slide: Slide, state_idx):
        animations = []
        for idx, state in enumerate(self.states):
            if idx == state_idx:
                animations += state.focus()
            else:
                animations += state.unfocus()
        for edge in self.edges:
            if edge.origin == self.states[state_idx] or edge.dest == self.states[state_idx]:
                animations += edge.focus(self.states[state_idx])
            else:
                animations += edge.unfocus()
        formula = Tex(r"$S3 = $")
        slide.play(
            *animations
        )

    def render(self, slide: Slide):
        for state in enumerate(self.states):
            if state[0] not in self.rendered_states:
                state_position_x = self.position[0] + (self.dimensions[0] / len(self.states)) * (state[0] + 0.5)
                state_position_y = self.position[1] + self.dimensions[0] / 2
                state[1].move_to(np.array([state_position_x, state_position_y, 0]))
                state[1].render(slide)
                self.rendered_states.append(state[0])
        for edge in enumerate(self.edges):
            if edge[0] not in self.rendered_edges:
                edge[1].render(slide)
                self.rendered_edges.append(edge[0])

class QueueVisualization(Slide):
    def construct(self):
        width = 10
        height = 10
        queue = Queue(np.array([width / -2, height / -2]), np.array([width, height]))
        queue.add_state(r"\pi_1", r'Un\ hilo\ de\ transferencia')
        queue.add_state(r"\pi_2", r'Dos\ hilo\ de\ transferencia')
        queue.add_state(r"\pi_3", r'1\ hilo\ de\ transferencia,\ 1\ hilo\ de\ cashout')
        queue.add_state(r"\pi_4", r'Test')
        queue.render(self)
        self.wait()
        self.next_slide()
        queue.add_edge(0, 1, r"$\lambda = 4$")
        queue.add_edge(1, 0, r"$\mu = 2$")
        queue.render(self)
        self.wait()
        self.next_slide()
        queue.add_edge(1, 2, r"$\lambda = 1.4$")
        queue.add_edge(2, 1, r"$\mu = 2$")
        queue.render(self)
        self.wait()
        self.next_slide()
        queue.add_edge(3, 2, r"$\lambda = 4$")
        queue.add_edge(2, 3, r"$\mu = 2$")
        queue.render(self)
        self.wait()
        self.next_slide()
        queue.focus_state(self, 2)
        self.wait()
        self.next_slide()
