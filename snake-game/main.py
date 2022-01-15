from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scorecard import ScoreCard
import math
import time

turtle = Turtle()
snake = Snake()
food = Food()
scorecard = ScoreCard()

screen = Screen()
# Screen setup
screen.title("Snake Game")
screen.screensize(500, 500)
screen.bgcolor("black")
screen.tracer(0)

snake.create_snake()
game_is_on = True

screen.listen()
screen.onkey(snake.move_up, "w")
screen.onkey(snake.move_down, "s")
screen.onkey(snake.turn_left, "a")
screen.onkey(snake.turn_right, "d")

food.random_position()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()  # This refresh has to be last otherwise the score will be added twice
        snake.adding_segment()  # Adding a new segment to the snake
        scorecard.score_increase()

    # Detect collision with the walls
    elif snake.head.xcor() > 300 or snake.head.ycor() > 300 or \
            snake.head.xcor() < -300 or snake.head.ycor() < -300:
        game_is_on = False
        scorecard.game_over()
    else:
        for segment in snake.segments[1:]:
            #     if segment == snake.head:
            #         pass
            #     elif snake.head.distance(segment) < 10:
            #         game_is_on = False
            #         scorecard.game_over()
            if snake.head.distance(segment) < 10:  # Use slicing method
                game_is_on = False
                scorecard.game_over()

screen.exitonclick()
