from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.create_ball()
        self.move_speed = 0.1
        self.move_speed_increaser = 0.9


    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        if randint(1, 2) == 1:
            self.x_move *= -1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_off_wall(self):
        self.y_move *= -1


    def bounce_off_paddle(self):
        self.x_move *= -1
        self.move_speed *= self.move_speed_increaser


    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1
        if randint(1, 2) == 1:
            self.y_move *= -1
        self.move_speed = 0.1 