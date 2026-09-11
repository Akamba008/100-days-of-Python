from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for snake in range(3):
            snake_part = Turtle("square")
            self.squares.append(snake_part)
            snake_part.color("white")
            snake_part.penup()
        for square in range(1, len(self.squares) - 1):
            prev_square = self.squares[square - 1]
            self.squares[square].goto(prev_square.xcor() - 20, prev_square.ycor())

    def move(self):
        for seg_num in range(len(self.squares) - 1, 0, -1):
            new_x_cor = self.squares[seg_num - 1].xcor()
            new_y_cor = self.squares[seg_num - 1].ycor()
            self.squares[seg_num].goto(new_x_cor, new_y_cor)
        self.head.forward(MOVE_DISTANCE)

    def increase_length(self):
        snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.penup()
        self.squares.append(snake_part)
        new_square = len(self.squares)-1
        new_x_cor = self.squares[new_square - 1].xcor()
        new_y_cor = self.squares[new_square - 1].ycor()
        snake_part.goto(new_x_cor, new_y_cor)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)