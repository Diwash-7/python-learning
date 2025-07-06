
from manim import *


class test (Scene) :
    def construct (self):
        t = Text("Your Name").scale(2)
        self.play(Write(t))
        self.wait(3)