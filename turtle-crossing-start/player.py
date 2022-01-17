import turtle
from turtle import Turtle
import random

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
turtle.tracer(0)


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.penup()

        self.shape("turtle")
        self.goto_position()
        self.setheading(90)

    def turtle_move(self):
        self.forward(MOVE_DISTANCE)

    def goto_position(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


