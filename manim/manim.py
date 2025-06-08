from manim import *


class test (Scene) :
    def construct (self):
        obj = Rectangle(height = 0.5  ,  width = 0.5)
        self.play(Write(obj))
        self.wait(3)