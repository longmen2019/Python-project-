from turtle import Turtle, Screen
import time
from paddle import Paddle
from scoreboard import ScoreBoard
from ball import Ball

turtle = Turtle()
screen = Screen()
screen.tracer(0)  # to turn off the animation of the paddle
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

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()  # to turn off the animation of the paddle
    ball.ball_move()  # to get the ball move

    # check ball collision with the paddle
    # right paddle
    if (ball.xcor() > 290 and ball.xcor() < 300) and (ball.ycor() < paddle_right.ycor() + 40
                                                      and ball.ycor() > paddle_right.ycor() - 40):
        ball.setx(360)
        ball.dx *= -1
    # left paddle
    if (ball.xcor() < -290 and ball.xcor() > -300) and (ball.ycor() < paddle_left.ycor() + 40
                                                        and ball.ycor() > paddle_left.ycor() - 40):
        ball.setx(-360)
        ball.dx *= -1
    else:
        ball.hit_wall()


screen.exitonclick()
