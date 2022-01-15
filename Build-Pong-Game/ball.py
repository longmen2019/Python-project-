from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.color(random.choice(["blue", "red", "green", "white", "yellow"]))
        self.speed(40)

    # def ball_move(self):

