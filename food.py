import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.shapesize(0.7, 0.7)
        self.rand_loc()

    def rand_loc(self):
        new_x = random.randint(-355, 355)
        new_y = random.randint(-300, 300)
        self.goto(new_x, new_y)

    def reset(self):
        self.rand_loc()