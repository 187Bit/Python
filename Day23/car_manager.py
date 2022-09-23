from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.car_list = []
        self.hideturtle()
        self.initialise_starter_cars()
        self.move_increase = 0 # how much the speed should increase for each new level

    def initialise_starter_cars(self):

        for i in range(0, 16):
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.turtlesize(stretch_len = 2)
            random_xposition = random.randint(-280, 280)
            random_yposition = random.randint(-240, 240)
            random_position = (random_xposition, random_yposition)
            car.setposition(random_position)
            self.car_list.append(car)


    def create_car(self):
        """Creates a single car at a random position with a random color from the COLORS list."""
        
        generate_car = random.randint(1,6)

        if generate_car == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.turtlesize(stretch_len = 2)
            random_yposition = random.randint(-240, 240)
            car.setposition(300, random_yposition)
            self.car_list.append(car)
        

    def move(self):
        
        for car in self.car_list:

            car.backward(STARTING_MOVE_DISTANCE + self.move_increase)

    def next_level(self):

        self.move_increase += 5
        
