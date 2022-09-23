import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Crossy Turtle")
player = Player()
cars = CarManager()
scoreboard = Scoreboard()


game = True

while game:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    
    screen.onkeypress(key = "Up", fun= player.move) # if the player pressed the up key, the function player.move will be triggered

    cars.move()
    cars.create_car()

    if player.ycor() > 280:
            player.setposition(0, -280)
            scoreboard.update()
            cars.next_level()
            
    
    for car in cars.car_list:
            if car.distance(player) < 25:
                scoreboard.game_over()
                game = False


screen.exitonclick()
    
