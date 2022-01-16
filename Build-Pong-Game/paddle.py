from turtle import Turtle
import random

COLOR = ['white', 'yellow', 'blue']


class Paddle(Turtle):
    def __init__(self):
        super(Paddle, self).__init__()

        self.color(random.choice(COLOR))
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed(0)  # Get the paddle to the exact goto location

    def right_paddle(self):
        # self.speed(0)
        self.goto(350, 0)

    def left_paddle(self):
        self.goto(-350, 0)

    # move paddle
    def paddle_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)

    def paddle_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)