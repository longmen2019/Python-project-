from turtle import Turtle

ALIGN = "CENTER"
FONT = ('Courier', 40, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.score = 0
        self.speed(0)

    def right_score(self):
        self.penup()
        self.color("red")
        # self.shape("square")
        self.goto(-50, 250)
        self.hideturtle()
        self.clear()
        self.write(f"L:{self.score}| ", False, ALIGN, FONT)
        self.score += 1

    def left_score(self):
        self.penup()
        self.color("white")
        # self.shape("square")
        self.goto(50, 250)
        self.hideturtle()
        self.clear()
        self.write(f"R:{self.score}", False, ALIGN, FONT)
        self.score += 1

    def increase_score(self):
        self.score += 1
