from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import ScoreBoard
from ball import Ball

turtle = Turtle()
screen = Screen()
paddle_right = Paddle()
paddle_left = Paddle()
score_right = ScoreBoard()
score_left = ScoreBoard()
ball = Ball()

# Set Up The Main Screen
screen.title("Pong Game")
screen.bgcolor("black")
screen.screensize(600, 600)

# Right and Left Score
score_right.right_score()
score_left.left_score()

# Right and Left Paddle
paddle_right.right_paddle()
paddle_left.left_paddle()

screen.listen()
screen.onkey(paddle_right.paddle_up, "o")
screen.onkey(paddle_right.paddle_down, "l")
screen.onkey(paddle_left.paddle_up, "w")
screen.onkey(paddle_left.paddle_down, "s")




screen.exitonclick()
