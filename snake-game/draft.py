from turtle import Turtle, Screen
import time

snake1 = Turtle()
snake2 = Turtle()
snake3 = Turtle()
screen = Screen()
screen.tracer(0)

# Screen setup
screen.title("Snake Game")
screen.screensize(500, 500)
screen.bgcolor("black")

snake1.shape("square")
snake2.shape("square")
snake3.shape("square")

snake1.color("white")
snake2.color("white")
snake3.color("white")

snake1.pensize(20)
snake2.pensize(20)
snake3.pensize(20)

snake1.speed(1)
snake2.speed(1)
snake3.speed(1)

snake1.goto(0, 0)
snake2.goto(-20, 0)
snake3.goto(-40, 0)

still_play = True


def move_forward():
    snake1.penup()
    snake1.forward(10)
    snake1.clear()
    snake2.penup()
    snake2.forward(10)
    snake2.clear()
    snake3.penup()
    snake3.forward(10)
    snake3.clear()
    time.sleep(0.1)
    screen.update()


def move_up():
    snake1.penup()
    snake1.setheading(90)
    snake1.forward(40)
    snake1.clear()
    snake2.penup()
    snake2.forward(20)
    snake2.setheading(90)
    snake2.forward(20)
    snake2.clear()
    snake3.penup()
    snake3.forward(40)
    snake3.setheading(90)
    snake3.clear()
    time.sleep(0.1)
    screen.update()


def move_down():
    snake1.penup()
    snake1.setheading(-90)
    snake1.forward(40)
    snake1.clear()
    snake2.penup()
    snake2.forward(20)
    snake2.setheading(-90)
    snake2.forward(20)
    snake2.clear()
    snake3.penup()
    snake3.forward(40)
    snake3.setheading(-90)
    snake3.clear()
    time.sleep(0.1)
    screen.update()


def turn_left():
    snake1.penup()
    snake1.setheading(180)
    snake1.forward(40)
    snake1.clear()
    snake2.penup()
    snake2.forward(20)
    snake2.setheading(180)
    snake2.forward(20)
    snake2.clear()
    snake3.penup()
    snake3.forward(40)
    snake3.setheading(180)
    snake3.clear()
    time.sleep(0.1)
    screen.update()


def turn_right():
    snake1.penup()
    snake1.setheading(0)
    snake1.forward(40)
    snake1.clear()
    snake2.penup()
    snake2.forward(20)
    snake2.setheading(0)
    snake2.forward(20)
    snake2.clear()
    snake3.penup()
    snake3.forward(40)
    snake3.setheading(0)
    snake3.clear()
    time.sleep(0.1)
    screen.update()


screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")

Game_On = True
while Game_On:
    move_forward()
    if snake1.xcor() > 285 or snake1.ycor() > 285 or snake1.xcor() < -285 or snake1.ycor() < -285:
        Game_On = False
        print("Game Over")

screen.exitonclick()
