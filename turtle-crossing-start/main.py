import time
import random
from turtle import Screen
from player import Player
# from car_manager import CarManager
from car_manager2 import CarManager
from scoreboard import Scoreboard

POSITION = [(280, 200), (280, 150), (280, 100), (280, 50), (280, 0), (280, -50), (280, -100), (280, -150), (280, -200),
            (280, -150)]

SPEED = range(15)

turtle = Player()
screen = Screen()
screen.tracer(0)
car_manager = CarManager()
scoreboard = Scoreboard()
game_over = Scoreboard()

# # car_manager setup
# car_1 = CarManager()
# car_2 = CarManager()
# car_3 = CarManager()
# car_4 = CarManager()
# car_5 = CarManager()
# car_6 = CarManager()
# car_7 = CarManager()
# car_8 = CarManager()
# car_9 = CarManager()
# car_10 = CarManager()
# car_11 = CarManager()
# car_12 = CarManager()
# car_13 = CarManager()
#
# # car_1 setup
# car_1.penup()
# car_1.goto(random.choice(POSITION))
#
# # car_2 setup
# car_2.penup()
# car_2.goto(random.choice(POSITION))
#
# # car_3 setup
# car_3.penup()
# car_3.goto(random.choice(POSITION))
#
# # car_4 setup
# car_4.penup()
# car_4.goto(random.choice(POSITION))
#
# # car_5 setup
# car_5.penup()
# car_5.goto(random.choice(POSITION))
#
# # car_6 setup
# car_6.penup()
# car_6.goto(random.choice(POSITION))
#
# # car_7 setup
# car_7.penup()
# car_7.goto(random.choice(POSITION))
#
# # car_7 setup
# car_7.penup()
# car_7.goto(random.choice(POSITION))
#
# # car_8 setup
# car_8.penup()
# car_8.goto(random.choice(POSITION))
#
# # car_9 setup
# car_9.penup()
# car_9.goto(random.choice(POSITION))
#
# # car_10 setup
# car_10.penup()
# car_10.goto(random.choice(POSITION))
#
# # car_11 setup
# car_11.penup()
# car_11.goto(random.choice(POSITION))
#
# # car_12 setup
# car_12.penup()
# car_12.goto(random.choice(POSITION))
#
# # car_13 setup
# car_13.penup()
# car_13.goto(random.choice(POSITION))


#  Screen setup
screen.setup(width=600, height=600)
screen.tracer(0)

# Screen keyboard setup
screen.listen()
screen.onkey(turtle.turtle_move, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()
    for car in car_manager.all_car:
        if turtle.distance(car) < 20:
            game_is_on = False
            game_over.game_over()
    # Detect Successful Crossing
    # if turtle.ycor() > 300:
    #     turtle.goto(0, -280)
    if turtle.finish_line():
        scoreboard.increase_level()
        car_manager.next_level()
        turtle.goto_position()
        # car_manager.create_car()










    # car_1.backward(random.choice(SPEED))
    # car_2.backward(random.choice(SPEED))
    # car_3.backward(random.choice(SPEED))
    # car_4.backward(random.choice(SPEED))
    # car_5.backward(random.choice(SPEED))
    # car_6.backward(random.choice(SPEED))
    # car_7.backward(random.choice(SPEED))
    # car_8.backward(random.choice(SPEED))
    # car_9.backward(random.choice(SPEED))
    # car_10.backward(random.choice(SPEED))
    # car_11.backward(random.choice(SPEED))
    # car_12.backward(random.choice(SPEED))
    # car_13.backward(random.choice(SPEED))
    #
    # if car_1.xcor() < -230:
    #     car_1.penup()
    #     car_1.goto(random.choice(POSITION))
    #     car_1.backward(random.choice(SPEED))
    #
    # if car_2.xcor() < -230:
    #     car_2.penup()
    #     car_2.goto(random.choice(POSITION))
    #     car_2.backward(random.choice(SPEED))
    # if car_3.xcor() < -230:
    #     car_3.penup()
    #     car_3.goto(random.choice(POSITION))
    #     car_3.backward(random.choice(SPEED))
    # if car_4.xcor() < -230:
    #     car_4.penup()
    #     car_4.goto(random.choice(POSITION))
    #     car_4.backward(random.choice(SPEED))
    # if car_5.xcor() < -230:
    #     car_5.penup()
    #     car_5.goto(random.choice(POSITION))
    #     car_5.backward(random.choice(SPEED))
    # if car_6.xcor() < -230:
    #     car_6.penup()
    #     car_6.goto(random.choice(POSITION))
    #     car_6.backward(random.choice(SPEED))
    # if car_7.xcor() < -230:
    #     car_7.penup()
    #     car_7.goto(random.choice(POSITION))
    #     car_7.backward(random.choice(SPEED))
    # if car_8.xcor() < -230:
    #     car_8.penup()
    #     car_8.goto(random.choice(POSITION))
    #     car_8.backward(random.choice(SPEED))
    # if car_9.xcor() < -230:
    #     car_9.penup()
    #     car_9.goto(random.choice(POSITION))
    #     car_9.backward(random.choice(SPEED))
    # if car_10.xcor() < -230:
    #     car_10.penup()
    #     car_10.goto(random.choice(POSITION))
    #     car_10.backward(random.choice(SPEED))
    # if car_11.xcor() < -230:
    #     car_11.penup()
    #     car_11.goto(random.choice(POSITION))
    #     car_11.backward(random.choice(SPEED))
    # if car_12.xcor() < -230:
    #     car_12.penup()
    #     car_12.goto(random.choice(POSITION))
    #     car_12.backward(random.choice(SPEED))
    # if car_13.xcor() < -230:
    #     car_13.penup()
    #     car_13.goto(random.choice(POSITION))
    #     car_13.backward(random.choice(SPEED))
screen.exitonclick()