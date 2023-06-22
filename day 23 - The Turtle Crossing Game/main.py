import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    # for car in car_manager.all_cars:
    #     if car.xcor() > -320:
    #         car.forward(cars_speed)

    if player.ycor() > 280:
        player.goto(0, -280)
        car_manager.increase_speed()
        scoreboard.level += 1
        scoreboard.track_level()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False




screen.exitonclick()
