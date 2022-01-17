from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
    def __init__(self):

        super(CarManager, self).__init__()

        self.color(random.choice(COLORS))
        self.forward(STARTING_MOVE_DISTANCE)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)  # by default a turtle is 20px in size

