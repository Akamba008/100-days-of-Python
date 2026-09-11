from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="What turtle will win the race? Enter a color: ")

y_axis = [-30, 30, -60, 60, 0, 90]
colors = ["red", "green", "blue", "orange", "black", "brown"]
turtles = []
referee =  Turtle()
referee.up()
referee.goto(230,120)
referee.down()
referee.right(90)
referee.forward(200)
referee.hideturtle()

for turtle_index in range(6):
    racer = Turtle()
    racer.penup()
    racer.shape("turtle")
    turtle_color = random.choice(colors)
    racer.color(turtle_color)
    colors.remove(turtle_color)
    starting_position = random.choice(y_axis)
    racer.goto(-230, starting_position)
    y_axis.remove(starting_position)
    racer.speed(1)
    turtles.append(racer)
random.shuffle(turtles)

def finished_race(turtle):
    if turtle.xcor() >= 230:
        winning_color = turtle.pencolor()
        if winning_color == user_bet:
            print(f"Your bet on {winning_color} won!")
        else:
            print(f"{winning_color} won. Your bet on {user_bet} lost.")
        return True
    return False

race_over =  False
while not race_over:
    for animal in turtles:
        rand_distance = random.randint(10,50)
        animal.forward(rand_distance)
        race_over = finished_race(animal)
        if race_over:
            break
    random.shuffle(turtles)

screen.exitonclick()