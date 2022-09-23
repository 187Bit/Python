from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle): #inherits from turtle module the Turtle class
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.setposition(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)
