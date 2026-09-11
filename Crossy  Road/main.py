import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen_dimension = (600,600)
screen.setup(screen_dimension[0], screen_dimension[1])
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager(screen_dimension)
screen.listen()

screen.onkeypress(key="w", fun=player.move_up)
screen.onkeypress(key="s", fun=player.move_down)
screen.onkeypress(key="a", fun=player.move_left)
screen.onkeypress(key="d", fun=player.move_right)
loop_counter = 0

game_is_on = True
while game_is_on:
    player.create_player()
    player.start_position()
    scoreboard.write_level()
    time.sleep(0.1)
    screen.update()

    while True:
        if loop_counter == 6:
            car_manager.create_cars()
            loop_counter = 0
        loop_counter += 1
        time.sleep(0.1)
        screen.update()
        car_manager.move_cars()

        for car in car_manager.car_list:
            dx = abs(car.xcor() - player.xcor())
            dy = abs(car.ycor() - player.ycor())
            if dx < 30 and dy < 15:  # roughly car half-width+buffer, half-height+buffer
                game_is_on = False
                break

        if not game_is_on:
            scoreboard.game_over()
            break

        if player.reach_end():
            car_manager.increase_speed()
            car_manager.reset_cars()
            scoreboard.increase_level()
            break

screen.exitonclick()

