from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.penup()
        self.color(random.choice(["blue", "red", "green", "white", "yellow"]))
        self.speed(40)

        self.dx = 5
        self.dy = -5

    def ball_move(self):
        self.setx(self.xcor() + self.dx)  # to move the ball
        self.sety(self.ycor() + self.dy)

    # def ball_move(self):

    def hit_wall(self):
        # the ball bounce back when hit y-axis
        if self.ycor() > 280:
            self.sety(280)
            self.dy *= -1
        if self.ycor() < -280:
            self.sety(-280)
            self.dy *= -1
        # the ball return to (0,0) when hit x-axis
        if self.xcor() > 600:
            self.goto(0, 0)
            self.dy *= -1
        if self.xcor() < -600:
            self.goto(0, 0)
            self.dy *= -1
