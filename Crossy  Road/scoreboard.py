from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONT_COLOR = "black"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280,265)


    def write_level(self):
        self.clear()
        self.color(FONT_COLOR)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0,265)
        self.color(FONT_COLOR)
        self.write(f"Game Over!", align="center", font=FONT)
