import turtle
from turtle import Turtle, Screen
import random


screen = Screen()

screen.title("Hist Painting Extraction Exercise")

color_rgb = [(236, 225, 199), (215, 219, 229), (241, 213, 231), (206, 155, 104), (211, 237, 219), (105, 111, 130),
             (137, 141, 160), (221, 216, 113), (180, 76, 36), (201, 141, 174), (182, 158, 31), (100, 106, 186),
             (12, 21, 65), (234, 162, 201), (9, 42, 17), (139, 167, 148), (230, 70, 44), (215, 64, 90), (149, 75, 96),
             (202, 16, 4), (39, 32, 10), (89, 116, 98), (37, 37, 131), (199, 13, 35), (230, 215, 5), (239, 170, 156),
             (178, 175, 233), (43, 15, 41), (166, 213, 172), (107, 144, 112), (35, 82, 41), (254, 5, 21), (82, 81, 21),
             (164, 202, 208), (98, 139, 148), (253, 9, 5), (18, 83, 96), (58, 48, 212)]

# color_rgb_tuple = tuple(color_rgb)
# random_color = random.choice(color_rgb_tuple)
#
# random_color2 = turtle.color(random_color)
# print(random_color2)

screen.colormode(255)  # use this to operate rbg color in python


# color = random.choice(color_rgb)
# color_rgb = 10


def first_position():
    # first start the turtle position
    turtle.hideturtle()
    turtle.setheading(225)
    turtle.penup()
    turtle.forward(400)
    # first draw of line
    turtle.setheading(360)
    turtle.speed("fastest")
    for i in range(20):
        # for color in color_rgb:
        color = random.choice(color_rgb)
        turtle.dot(15, color)
        turtle.forward(20)
        turtle.penup()
    for j in range(9):
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(400)
        turtle.setheading(360)
        for i in range(20):
            # get the random color from color_rgb
            color = random.choice(color_rgb)
            turtle.dot(15, color)
            turtle.forward(20)
            turtle.penup()


first_position()

screen.exitonclick()
# # Third line
# turtle.setheading(90)
# turtle.forward(50)
# turtle.setheading(180)
# turtle.forward(400)
# turtle.setheading(360)
# for i in range(20):
#     turtle.forward(20)
#     turtle.penup()
#     turtle.dot(10, color)
# # Fourth line
# turtle.setheading(90)
# turtle.forward(50)
# turtle.setheading(180)
# turtle.forward(400)
# turtle.setheading(360)
# for i in range(20):
#     turtle.forward(20)
#     turtle.penup()
#     turtle.dot(10, color)
# # Fifth line
# turtle.setheading(90)
# turtle.forward(50)
# turtle.setheading(180)
# turtle.forward(400)
# turtle.setheading(360)
# for i in range(20):
#     turtle.forward(20)
#     turtle.penup()
#     turtle.dot(10, color)
# # Sixth line
# turtle.setheading(90)
# turtle.forward(50)
# turtle.setheading(180)
# turtle.forward(400)
# turtle.setheading(360)
# for i in range(20):
#     turtle.forward(20)
#     turtle.penup()
#     turtle.dot(10, color)
# # Seventh line
# turtle.setheading(90)
# turtle.forward(50)
# turtle.setheading(180)
# turtle.forward(400)
# turtle.setheading(360)
# for i in range(20):
#     turtle.forward(20)
#     turtle.penup()
#     turtle.dot(10, color)
# # Eight line
# turtle.setheading(90)
# turtle.forward(50)
# turtle.setheading(180)
# turtle.forward(400)
# turtle.setheading(360)
# for i in range(20):
#     turtle.forward(20)
#     turtle.penup()
#     turtle.dot(10, color)
# # Ninth line
# turtle.setheading(90)
# turtle.forward(50)
# turtle.setheading(180)
# turtle.forward(400)
# turtle.setheading(360)
# for i in range(20):
#     turtle.forward(20)
#     turtle.penup()
#     turtle.dot(10, color)
# # Tenth line
# turtle.setheading(90)
# turtle.forward(50)
# turtle.setheading(180)
# turtle.forward(400)
# turtle.setheading(360)
# for i in range(20):
#     turtle.forward(20)
#     turtle.penup()
#     turtle.dot(10, color)
