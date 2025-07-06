from manim import * 
import numpy as np
from manim_slides import Slide

def middle_point(a, b):
    return (a + b) / 2

ORIGIN = np.array([0, 0, 0])
STATE_RADIUS = 0.5
LABEL_ORIGIN = np.array([0.0, float(5 * STATE_RADIUS), 0.0])

class State:
    def __init__(self, label: str) -> None:
        self.label = label
        self.position = ORIGIN
        self.connected_edges = []
    
    def move_to(self, position):
        self.position = position

    def render(self, slide: Slide):
        slide.play(Write(
            LabeledDot(self.label, STATE_RADIUS, point=self.position),
        ))

class Edge:
    def __init__(self, origin, dest, label) -> None:
        self.origin = origin
        self.dest = dest
        self.label = label

    def render(self, slide):
        direction = 1 if self.origin.position[0] > self.dest.position[0] else -1
        slide.play(Write(
            arrow := CurvedArrow(
                self.origin.position + np.array([0, STATE_RADIUS * direction, 0]),
                self.dest.position + np.array([0, STATE_RADIUS * direction, 0])
            )
        ))
        label = Tex(self.label, font_size=36)
        label_offset = (arrow.height * 1.5 + STATE_RADIUS) * direction
        label_position = middle_point(self.origin.position, self.dest.position) + np.array([0, label_offset, 0])
        label.move_to(LABEL_ORIGIN * direction)
        slide.play(Write(label))
        slide.play(label.animate.move_to(label_position))

class Queue:
    def __init__(self, position, canvas_dimensions) -> None:
        self.states = []
        self.edges = []
        self.dimensions = canvas_dimensions
        self.position = position

    def add_state(self, label: str):
        state = State(label)
        self.states.append(state)

    def add_edge(self, origin_idx, dest_idx, label):
        edge = Edge(self.states[origin_idx], self.states[dest_idx], label)
        self.edges.append(edge)

    def render(self, slide: Slide):
        for state in enumerate(self.states):
            state_position_x = self.position[0] + (self.dimensions[0] / len(self.states)) * (state[0] + 0.5)
            state_position_y = self.position[1] + self.dimensions[0] / 2
            state[1].move_to(np.array([state_position_x, state_position_y, 0]))
            state[1].render(slide)
        for edge in self.edges:
            edge.render(slide)

class QueueVisualization(Slide):
    def construct(self):
        width = 10
        height = 10
        queue = Queue(np.array([width / -2, height / -2]), np.array([width, height]))
        queue.add_state("S1")
        queue.add_state("S2")
        queue.add_state("S3")
        queue.add_state("S4")
        queue.add_edge(0, 1, r"$\lambda = 4$")
        queue.add_edge(1, 0, r"$\mu = 2$")
        queue.add_edge(1, 2, r"$\lambda = 1.4$")
        queue.add_edge(2, 1, r"$\mu = 2$")
        queue.add_edge(3, 2, r"$\lambda = 4$")
        queue.render(self)
        self.wait()
        self.next_slide()
