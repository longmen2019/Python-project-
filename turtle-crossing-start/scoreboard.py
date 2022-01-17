from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color = "white"
        self.penup()
        self.goto(-220, 240)
        self.player_level()

    def player_level(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "Center", FONT)

    def increase_level(self):
        self.level += 1
        self.player_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, "Center", FONT)
