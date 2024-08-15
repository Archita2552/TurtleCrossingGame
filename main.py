from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen=Screen()
screen.setup(600,600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.listen()

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()
screen.onkeypress(player.t_forward,"Up")
screen.onkeypress(player.t_backward,"Down")




game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    car_manager.create_car()
    car_manager.move_cars()

    #detect collision
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()
    #detect successful crossing
    if player.is_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()







screen.exitonclick()