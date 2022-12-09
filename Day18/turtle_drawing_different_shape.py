import random
from turtle import Turtle, Screen # imports the Turtle and Screen class from the turtle module, much more convenient because you do not have to write turtle.Turtle etc.
import turtle 

new_turtle = Turtle() # Creates a new_turtle object from the Turtle class

new_turtle.shape("turtle") # Changes the shape of the new_turtle object to "turtle"
new_turtle.color("forest green") # Changes the color of the new_turtle object to "green"

new_turtle.speed(2)

def change_color():

    number_list = []

    for i in range(0,3):
        new_number = random.randint(0,255)
        number_list.append(new_number)

    return number_list


for i in range(3,11):

    returned = change_color()
    turtle.colormode(255)
    new_turtle.pencolor((returned[0],returned[1],returned[2]))

    for l in range(0,i):
        new_turtle.right(360/i)
        new_turtle.forward(100)

# for i in range(0,3): # Creates a triangle with the dimensions of 100x100
#     new_turtle.right(120)
#     new_turtle.forward(100)


# for i in range(0,4): # Creates a square with a stroke length of 100
#     new_turtle.right(90)
#     new_turtle.forward(100)
    
# for i in range(0,5): # Creates a pentagon with a stroke length of 100
#     new_turtle.right(72)
#     new_turtle.forward(100)


# for i in range(0,6): # Creates a hexagon a stroke length of 100
#     new_turtle.right(60)
#     new_turtle.forward(100)

# for i in range(0,7): # Creates a heptagon a stroke length of 100
#     new_turtle.right(51.4)
#     new_turtle.forward(100)


# for i in range(0,8): # Creates a octagon a stroke length of 100
#     new_turtle.right(45)
#     new_turtle.forward(100)

# for i in range(0,9): # Creates a nonagon a stroke length of 100
#     new_turtle.right(40)
#     new_turtle.forward(100)

# for i in range(0,10): # Creates a decagon a stroke length of 100
#     new_turtle.right(36)
#     new_turtle.forward(100)


screen = Screen()
screen.exitonclick()