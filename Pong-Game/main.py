from turtle import Screen
import time
from paddles import Paddles
from referee import Referee
from ball import Ball
from random import randint


screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

referee = Referee()
paddle1 = Paddles((350,0))
paddle2 = Paddles((-350,0))
ball = Ball()

screen.listen()
screen.onkeypress(paddle1.up, "Up")
screen.onkeypress(paddle1.down, "Down")
screen.onkeypress(paddle2.up, "w")
screen.onkeypress(paddle2.down, "s")
screen.onkeypress(paddle2.up, "W")
screen.onkeypress(paddle2.down, "S")

game_running = True
while game_running:
    screen.update()
    time.sleep(ball.move_speed)

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_off_wall()

    #Detect collision with right paddle
    elif ball.distance(paddle1) < 50 and ball.xcor() > 320:
        ball.bounce_off_paddle()

    # Detect collision with left paddle
    elif ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_off_paddle()

    #Handle what happens when left paddle misses
    elif ball.xcor() > 380:
        ball.reset_position()
        referee.l_score()

    #Handle what happens when left paddle misses
    elif ball.xcor() < -380:
        ball.reset_position()
        referee.r_score()

    ball.move()


print("Game Over")


screen.exitonclick()