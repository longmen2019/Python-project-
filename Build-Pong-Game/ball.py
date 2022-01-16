from turtle import Turtle
from scoreboard import ScoreBoard
import random

scoreboard = ScoreBoard()
class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.penup()
        self.color(random.choice(["blue", "red", "green", "white", "yellow"]))
        # self.speed(0)

        self.dx = random.choice([10, -10])
        self.dy = random.choice([-10, 10])

    def ball_move(self):
        self.setx(self.xcor() + self.dx)  # to move the ball
        self.sety(self.ycor() + self.dy)

    # def ball_move(self):

    def hit_wall(self):
        # the ball bounce back when hit y-axis
        if self.ycor() > 300:
            self.sety(300)
            self.dy *= -1
        if self.ycor() < -300:
            self.sety(-300)
            self.dy *= -1
        # the ball return to (0,0) when hit x-axis
        if self.xcor() > 400:
            scoreboard.increase_score()
            self.goto(0, 0)
            self.dy *= 1

            # the other player will have an opportunity to play after the ball miss the paddle
            self.dx *= -1
        if self.xcor() < -400:
            scoreboard.increase_score()
            self.goto(0, 0)
            self.dy *= -1
            # the other player will have an opportunity to play after the ball miss the paddle
            self.dx *= -1

