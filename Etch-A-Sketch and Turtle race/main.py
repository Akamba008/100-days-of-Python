from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

def move_forward():
    tom.forward(10)

screen.listen()
screen.onkeypress(move_forward, "space")


screen.exitonclick()