import turtle
from turtle import Turtle, Screen
import random

one = Turtle()
two = Turtle()
three = Turtle()
four = Turtle()
five = Turtle()

# Screen Setting
screen = Screen()
screen.title("Python Turtle Graphics")
screen.screensize(500, 500)

user_input = screen.textinput("user_input", "Which turtle would you bet on? ")

one.shape("turtle")
two.shape("turtle")
three.shape("turtle")
four.shape("turtle")
five.shape("turtle")

one.color("yellow")
two.color("blue")
three.color("red")
four.color("green")
five.color("black")

one.pensize(20)
two.pensize(20)
three.pensize(20)
four.pensize(20)
five.pensize(20)

one.penup()
one.goto(-240, 200)
two.penup()
two.goto(-240, 100)
three.penup()
three.goto(-240, 0)
four.penup()
four.goto(-240, -100)
five.penup()
five.goto(-240, -200)

destination = True
speed = [2, 3, 4, 5, 6]


def move_forward():
    global destination
    while destination:
        one.forward(random.choice(speed))
        two.forward(random.choice(speed))
        three.forward(random.choice(speed))
        four.forward(random.choice(speed))
        five.forward(random.choice(speed))
        if one.xcor() > 250:
            print("The Yellow Turtle has won")
            winner = "yellow"
            if user_input == winner:
                print("User's won")
            return
        elif two.xcor() > 250:
            print("The Blue Turtle has won")
            winner = "blue"
            if user_input == winner:
                print("User's won")
            return
        elif three.xcor() > 250:
            print("The Red Turtle has won")
            winner = "red"
            if user_input == winner:
                print("User's won")
            return
        elif four.xcor() > 250:
            print("The Green Turtle has won")
            winner = "green"
            if user_input == winner:
                print("User's won")
            return
        elif five.xcor() > 250:
            print("The Black Turtle has won")
            winner = "black"
            if user_input == winner:
                print("User's won")
            return


screen.listen()
screen.onkeypress(fun=move_forward, key="space")

screen.exitonclick()
