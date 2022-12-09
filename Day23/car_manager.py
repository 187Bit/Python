from turtle import Turtle # imports the Turtle class from the turtle module
import random # imports the random module

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"] # CONSTANT list with various colors in the form of strings
STARTING_MOVE_DISTANCE = 5


class CarManager(Turtle): # creates the class "Car Manager" which inherits from the Turtle class
    
    def __init__(self) -> None: # initialisation function
        super().__init__() # super initialisation for the inheritance of the Turtle class
        self.car_list = [] # creates an empty list called car_list
        self.hideturtle() # hides the turtle on the screen
        self.initialise_starter_cars() # calls the initialise_starter_cars function
        self.move_increase = 0 # how much the speed should increase for each new level, at the beginning the attribute is set to 0

    def initialise_starter_cars(self):

        """Spawns 15 squares (cars) with different colors at a random position on the screen."""

        for i in range(0, 16): # for loop in the range from 0 to 16
            car = Turtle("square") # creates a new turtle object from the Turtle class called car
            car.penup() # turtle no longer draws on screen when moving 
            car.color(random.choice(COLORS)) # changes the color of the square (car) to a random color from the COLORS constant list by using the random.chouice function
            car.turtlesize(stretch_len = 2) # strechtes the shape of the turtle object in the length by x 2
            random_xposition = random.randint(-280, 280) # gets a random value in the range from -280 to 280 by using the random.randint function and stores it in the random_xposition variable
            random_yposition = random.randint(-240, 240) # gets a random value in the range from -240 to 240 by using the random.randint function and stores it in the random_yposition variable
            random_position = (random_xposition, random_yposition) # puts both the random_xposition variable and the random_yposition variable in a tuple and stores it in the variable random_position
            car.setposition(random_position) # sets the position to the value stores inside random_position
            self.car_list.append(car) # appends the "car" turtle object to the "car_list" list


    def create_car(self):
        """Creates a single car at a random position with a random color from the COLORS list."""
        
        generate_car = random.randint(1,6)

        if generate_car == 1:
            car = Turtle("square")
            car.penup() # turtle no longer draws on screen when moving 
            car.color(random.choice(COLORS)) # changes the color of the square (car) to a random color from the COLORS constant list by using the random.chouice function
            car.turtlesize(stretch_len = 2)
            random_yposition = random.randint(-240, 240)  # gets a random value in the range from -240 to 240 by using the random.randint function and stores it in the random_yposition variable
            car.setposition(300, random_yposition)  # sets the position to 300 and the value stored inside random_yposition
            self.car_list.append(car) # appends the "car" turtle object to the "car_list" list
        

    def move(self):

        """Moves every turtle object stored in the 'car_list' list backwards by the constant STARTING_MOVE_DISTANCE and the move_increase variable."""
        
        for car in self.car_list: # Loops trough every object that is stored in the list "car_list"

            car.backward(STARTING_MOVE_DISTANCE + self.move_increase)  # Moves the object backwards by the constant STARTING_MOVE_DISTANCE and the move_increase variable

    def next_level(self):

        """Increases the variable move_increase by 5."""

        self.move_increase += 5
        
