from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score = 0
        with open("data.txt", "r") as highscore_file:
            highscore = int(highscore_file.read())
        self.highscore = highscore
        self.penup()
        self.goto(0,270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score}, High Score = {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):#
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)