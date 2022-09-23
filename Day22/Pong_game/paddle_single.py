from turtle import Turtle, position

class Paddle(Turtle):

    def __init__(self, position) -> None: # To add parameters into the class put it in the initialisation method
        super().__init__()
        self.create_paddle()
        self.set_position(position)
        # self is the object that gets created from the class
        

    def create_paddle(self):
        # paddle = Turtle("square") # because this call inherits from the turtle class a new_turtle get created automatically when creating a new objet
        self.shape("square")
        self.penup()
        self.color("white")
        self.turtlesize(stretch_wid= 5, stretch_len = 1)

    def set_position(self, position):
        self.setposition(position)
    	
    def move_up(self): # Methods always have a first parameter "self"
        y = self.ycor() + 20
        self.sety(y)
        
    def move_down(self):
        y = self.ycor() - 20
        self.sety(y)