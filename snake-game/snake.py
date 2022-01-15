from turtle import Turtle, Screen
import random

# snake1.goto(0, 0)
# snake2.goto(-20, 0)
# snake3.goto(-40, 0)
import food

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake(Turtle):
    def __init__(self):
        super(Snake, self).__init__()
        self.segments = []
        self.create_snake()
        # snake1 = Turtle()
        # snake2 = Turtle()
        # snake3 = Turtle()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POSITION:
            new_segment = Turtle("square")
            # snake1.shape("square")
            # snake2.shape("square")
            # snake3.shape("square")
            new_segment.color("white")
            # snake1.color("white")
            # snake2.color("white")
            # snake3.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        # def move_forward():
        #     snake1.penup()
        #     snake1.forward(10)
        #     snake1.clear()
        #     snake2.penup()
        #     snake2.forward(10)
        #     snake2.clear()
        #     snake3.penup()
        #     snake3.forward(10)
        #     snake3.clear()
        #     time.sleep(0.1)
        #     screen.update()
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

        # snake1.penup()
        # snake1.setheading(90)
        # snake1.forward(40)
        # snake1.clear()
        # snake2.penup()
        # snake2.forward(20)
        # snake2.setheading(90)
        # snake2.forward(20)
        # snake2.clear()
        # snake3.penup()
        # snake3.forward(40)
        # snake3.setheading(90)
        # snake3.clear()
        # time.sleep(0.1)
        # screen.update()

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    #     snake1.penup()
    #     snake1.setheading(-90)
    #     snake1.forward(40)
    #     snake1.clear()
    #     snake2.penup()
    #     snake2.forward(20)
    #     snake2.setheading(-90)
    #     snake2.forward(20)
    #     snake2.clear()
    #     snake3.penup()
    #     snake3.forward(40)
    #     snake3.setheading(-90)
    #     snake3.clear()
    #     time.sleep(0.1)
    #     screen.update()

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        # snake1.penup()
        # snake1.setheading(180)
        # snake1.forward(40)
        # snake1.clear()
        # snake2.penup()
        # snake2.forward(20)
        # snake2.setheading(180)
        # snake2.forward(20)
        # snake2.clear()
        # snake3.penup()
        # snake3.forward(40)
        # snake3.setheading(180)
        # snake3.clear()
        # time.sleep(0.1)
        # screen.update()

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def adding_segment(self):
        new_segment = Turtle("square")
        new_segment.color('orange')
        new_segment.penup()
        self.segments.append(new_segment)


