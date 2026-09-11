from turtle import Turtle, Screen, colormode
from random import *

tom = Turtle()
colormode(255)
angle_list = [0, 90, 180, 270]
tom.speed("fastest")
tom.pensize(7)

def colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

for movement in range(200):
    tom.color(colors())
    tom.setheading(choice(angle_list))
    tom.fd(25)












# SHAPES DRAWN OVER EACH OTHER IN A PPATTERN
# length_of_sides = 100
# sides = 3
# for shape in range(10):
#     angle = 360/sides
#     for side in range(sides):
#         tom.forward(length_of_sides)
#         tom.right(angle)
#     sides += 1
screen = Screen()
screen.exitonclick()
