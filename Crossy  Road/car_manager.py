from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5

MOVE_INCREMENT = 10


class CarManager():
    def __init__(self, position):
        self.car_list = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.move_increment = MOVE_INCREMENT
        self.position = position
        self.min_car_y = -(self.position[1]//2) + 60
        self.max_car_y = (self.position[1]//2) - 60
        self.starting_x_position = position[0]//2

    def create_cars(self):
        self.car_list.append(Turtle("square"))
        self.car_list[-1].penup()
        self.car_list[-1].color(choice(COLORS))
        self.car_list[-1].shapesize(stretch_wid=1, stretch_len=2)
        self.car_list[-1].setheading(180)
        starting_y_position = randint(self.min_car_y, self.max_car_y)
        self.car_list[-1].goto(self.starting_x_position, starting_y_position)

    def move_cars(self):
        for car in self.car_list:
            car.forward(self.move_distance)

    def increase_speed(self):
        self.move_distance += self.move_increment

    def reset_cars(self):
        for car in self.car_list:
            car.hideturtle()
        self.car_list.clear()