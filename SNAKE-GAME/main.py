from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_running = True
while game_running:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision between snake and food
    if snake.head.distance(food) < 15:
        food.refresh()
        screen.tracer(0)
        snake.increase_length()
        scoreboard.increase_score()

    #Detect collision with body
    for snake_part in snake.squares[1:]:
        if snake.head.distance(snake_part) < 15:
            game_running = False
            scoreboard.game_over()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_running = False
        scoreboard.game_over()





screen.exitonclick()