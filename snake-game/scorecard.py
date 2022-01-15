from turtle import Turtle


ALIGN = "Center"
FONT = ('Courier', 20, 'bold')
COLOR = "white"


class ScoreCard(Turtle):
    def __init__(self):
        super(ScoreCard, self).__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0, 250)
        self.write(f"Score: {self.score}", False, ALIGN, FONT)
        self.hideturtle()

    def score_increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, ALIGN, FONT)

    def game_over(self):
        # self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGN, FONT)

