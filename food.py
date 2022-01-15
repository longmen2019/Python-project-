from turtle import Turtle
import random

COLOR = ['red', 'green', 'yellow']
POSITION = range(-250, 250)


class Food(Turtle):
    def __init__(self):
        super(Food, self).__init__()
        self.color(random.choice(COLOR))
        self.shape("circle")

    def random_position(self):
        self.penup()
        self.goto(random.choice(POSITION), random.choice(POSITION))

    def refresh(self):
        self.color(random.choice(COLOR))
        self.goto(random.choice(POSITION), random.choice(POSITION))

    # def food_collision(self):

# food2 = Turtle()
# food2.color("white")
# food2.shape("circle")
# x = range(250)
# y = range(250)
# food2.penup()
# food2.goto(random.choice(x), random.choice(y))
