from random import randint
import turtle as t

tom = t.Turtle()
t.colormode(255)
screen = t.Screen()
tom.pensize(5)

def to_line_above(num):
    tom.penup()
    tom.left(90)
    tom.fd(num)
    tom.left(90)
    tom.fd(num)
    tom.right(180)

def colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

def painting(size):
    for i in range(size):
        for j in range(size):
            tom.color(colors())
            tom.circle(1)
            tom.up()
            tom.forward(50)
            tom.down()
        to_line_above(50)


painting(4)
screen.exitonclick()