from turtle import Turtle
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
GAME_SCREEN_Y = SCREEN_HEIGHT // 2 - 25
SCORE_POSITION_RIGHT = ((SCREEN_WIDTH // 2) // 2 // 2, SCREEN_HEIGHT // 2 - 100)
SCORE_POSITION_LEFT = ((-SCREEN_WIDTH // 2) // 2 // 2, SCREEN_HEIGHT // 2 - 100)


class Referee(Turtle):
    def __init__(self):
        super().__init__()
        self.ref = Turtle()
        self.ref.color("white")
        self.ref.penup()
        self.ref.hideturtle()
        self.score_1 = 0
        self.score_2 = 0
        self.demarcate()
        self.scoreboard()


    def demarcate(self):
        self.color("white")
        self.goto(0, GAME_SCREEN_Y)
        self.goto(0, -GAME_SCREEN_Y)
        self.hideturtle()

    def scoreboard(self):
        self.ref.clear()
        self.ref.goto(SCORE_POSITION_RIGHT)
        self.ref.write(self.score_1, align ="center", font=("Arial", 80, "normal"))
        self.ref.goto(SCORE_POSITION_LEFT)
        self.ref.write(self.score_2, align="center", font=("Arial", 80, "normal"))


    def r_score(self):
        self.score_1 += 1
        self.scoreboard()

    def l_score(self):
        self.score_2 += 1
        self.scoreboard()