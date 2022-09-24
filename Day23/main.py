import time
from turtle import Screen # imports the Screen class from the turtle module
from player import Player # imports the Player class from the player module
from car_manager import CarManager # imports the CarManager class from the Car_manager module 
from scoreboard import Scoreboard # imports the Scoreboard class from the scoreboard module

screen = Screen() # creates a new screen object from the Screen class
screen.setup(width=600, height=600) # sets the screens dimensions to a width of 600 and a height of 600
screen.tracer(0) # sets the screen tracer to 0
screen.title("Crossy Turtle") # changes the screen title to "Crossy Turtle"
player = Player() # creates a player object from the Player class
cars = CarManager() # creates a cars object from the CarManager() class
scoreboard = Scoreboard() # creates a scoreboard object from the Scoreboard() class


game = True # sets the boolean "game" to True

while game: # while game is true 

    time.sleep(0.1) # sets the amount of sleep time between each loops to 0.1 seconds
    screen.update() # updates the screen
    screen.listen() # screen object starts listening to inputs
    
    screen.onkeypress(key = "Up", fun= player.move) # if the player pressed the up key, the function player.move will be triggered

    cars.move() # calls the move function from the cars object
    cars.create_car() # calls the "create_car" function from the cars object

    if player.ycor() > 280: # checks if the players y coordinate is over 280
            player.setposition(0, -280) # sets the positio of the player to 0 and -280
            scoreboard.update() # calls the update function from the scoreboard object
            cars.next_level() # calls the next_level function from the cars object
            
    
    for car in cars.car_list: # loops through every turtle object in the "car_list" list
            if car.distance(player) < 25: # checks it the the objects distances to the player is lower that 25
                scoreboard.game_over() # calls the game_over function from the scoreboard function
                game = False # sets game to false


screen.exitonclick() # calls the exitonclick function from the screen object
    
