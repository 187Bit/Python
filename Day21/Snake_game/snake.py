from turtle import Turtle, Screen

OFFSETS = [(0,0), (-20,0), (20, 0)] 
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
            
            self.add_segment(position)

    def move(self):

            for segment_number in range(len(self.all_squares)-1, 0, -1): # For loop that counts from length of all_squares - 1 to 0 in steps of -1 
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

    def add_segment(self, position):
        """Adds a segment at a given position."""
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.setposition(position)
        self.all_squares.append(new_square)

    def extend(self):
        """Adds a new segment to the snake."""
        self.add_segment(self.all_squares[-1].position()) # gets hold of the last segment in the list of all segments and its position (the parameter in the add_segment method and the argument in the call)