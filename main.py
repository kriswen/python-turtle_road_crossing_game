import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

MOVE_INCREMENT = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Road Crossing Game")
screen.tracer(0)
screen.listen()

player = Player()
screen.onkeypress(player.up, "Up")
# TODO 1: allow user to move left/right

car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    # display scoreboard
    scoreboard.display_score()
    # detect collision: if player's center(20x20) is < 20 away from car's center (20x40)
    for car in car_manager.all_cars:
        if player.distance(car.xcor(), car.ycor()) <= 20:
            game_is_on = False
            scoreboard.game_over()

    # detect if player reached the top
    if player.check_is_finish():
        car_manager.level_up()
        scoreboard.level_up()
        player.reset_position()


screen.exitonclick()

