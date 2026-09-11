import turtle as t
from random import randint

tom = t.Turtle()
screen = t.Screen()
t.colormode(255)
tom.speed("fastest")
tom.color("red")

def colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


def spirograph(size_of_gap):
    for circle in range(int(360/size_of_gap)):
        tom.color(colors())
        tom.circle(100)
        current_position = tom.heading()
        tom.setheading(current_position + size_of_gap)

spirograph(1)

screen.exitonclick()