from turtle import Turtle, Screen

OFFSETS = [0, -20, 20] # alternatively you could create a list of tuples like OFFSETS =  [(0,0), (-20,0), (20,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):
        self.all_squares = []
        self.create_snake()
        self.head = self.all_squares[0]
        

    def create_snake(self): # Always include self in the methods you create
        for position in OFFSETS:
            
            new_square = Turtle("square")
            new_square.color("white")
            new_square.penup()
            new_square.setposition(position, 0)
            self.all_squares.append(new_square)

    def move(self):

            for segment_number in range(len(self.all_squares)-1, 0, -1):
                new_x = self.all_squares[segment_number - 1].xcor()
                new_y = self.all_squares[segment_number - 1].ycor()
                self.all_squares[segment_number].setposition(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)  

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
