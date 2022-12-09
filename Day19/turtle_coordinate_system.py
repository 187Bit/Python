from turtle import Turtle, Screen, forward
import random

new_screen = Screen()
new_screen.setup(width =1000, height = 800)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-250, -200, -150, 150, 200, 250]
all_turtles = []
race = False

for index in range(0,6): # for loop in the range of 0 to 5
    new_turtle = Turtle(shape = "turtle") # creates a new turtle object with the shape of a turtle, can be done separately too
    new_turtle.penup() # turtle does not draw when moving
    new_turtle.color(colors[index]) # change the color of the turtle to a color from the color list at the value of index
    new_turtle.setposition(x =-475, y = y_positions[index]) # sets the position of the turtle at the coordinates -470 and the value in the list y_positions at the index value
    all_turtles.append(new_turtle) # appends the new_turtle object to the list of all_turtles
    
user_input = new_screen.textinput(title = "Make your bet!", prompt= "Which turtle will win the race?") # creates a prompt windows and ask the user which turtle will win the race, returns a string

if user_input:
    race = True

while race:

    random_number = random.randint(0,10)
    random_index = random.randint(0,5)
    all_turtles[random_index].forward(random_number)

    for turtle in all_turtles:
       if turtle.xcor() > 475:
            race = False
            winner_turtle = turtle.pencolor()
            if winner_turtle == user_input:
                print(f"You won! The {winner_turtle} turtle is the winner.")
            else:
                print(f"You lost! The {winner_turtle} turtle is the winner.")



new_screen.exitonclick()