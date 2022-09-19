from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width= 1200, height= 1200)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0) # turns off the tracer
all_squares = []
offset = [0, -20, 20] # alternatively you could create a list of tuples like offsets =  [(0,0), (-20,0), (20,0)]

# First step: create snake body
for position in offset:
    new_square = Turtle("square")
    new_square.color("white")
    new_square.penup()
    new_square.setposition(position, 0)
    all_squares.append(new_square)

# Second step: moving the snake 

screen.update()

game = True

while game:
    screen.update()
    time.sleep(0.1)

    for segment_number in range(len(all_squares)-1, 0, -1):
        new_x = all_squares[segment_number - 1].xcor()
        new_y = all_squares[segment_number - 1].ycor()
        all_squares[segment_number].setposition(new_x, new_y)
    all_squares[0].forward(20)
    all_squares[0].right(90)
    
# Third step: controllin the screen with keystrokes




screen.exitonclick()