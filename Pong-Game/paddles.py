from turtle import Turtle

class Paddles(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.create_right_paddle()

    def create_right_paddle(self):
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.position)

    def up(self):
        prev_y = self.ycor()
        new_y = prev_y + 20
        self.goto(self.position[0], new_y)

    def down(self):
        prev_y = self.ycor()
        new_y = prev_y - 20
        self.goto(self.position[0], new_y)


