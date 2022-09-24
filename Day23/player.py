from turtle import Turtle # imports the Turtle class from the turtle module

STARTING_POSITION = (0, -280) # Starting position constant with a tuple that contains two values
MOVE_DISTANCE = 10 # Constant with the value 10
FINISH_LINE_Y = 280 # Constant with the value 280


class Player(Turtle): # Creates the "Player" class that inherits the Turtle class from the turtle module
    
    def __init__(self) -> None: # initialisation function
        super().__init__() # super initialisation for the inheritance of the Turtle class
        self.shape("turtle") # changes the shape of the turtle object to a turtle
        self.color("black") # changes the color of the turtle object wo black
        self.penup() # turtle no longer draws on screen when moving
        self.setheading(90) # sets the heading of the turtle to 90 degrees
        self.setposition(STARTING_POSITION) # sets the poistion of the turtle object to the tuple stored in the constant "STARTING POSITION"

    def move(self):

        """Moves the turtle object forward by the value stored in the constant MOVE_DISTANCE.""" 

        self.forward(MOVE_DISTANCE)
