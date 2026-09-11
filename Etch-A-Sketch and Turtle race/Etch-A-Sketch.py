from turtle import Screen, Turtle

tom = Turtle()
screen = Screen()

def move_forward():
    tom.forward(10)

def move_backward():
    tom.backward(10)

def turn_left():
    tom.left(10)

def turn_right():
    tom.right(10)

def clear_drawing():
    screen.reset()
    # tom.goto(0,0)

screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.onkeypress(clear_drawing, "c")

screen.exitonclick()