from turtle import Turtle, Screen # imports the Turtle and Screen class from the turtle module, much more convenient because you do not have to write turtle.Turtle etc.

new_turtle = Turtle() # Creates a new_turtle object from the Turtle class

new_turtle.shape("turtle") # Changes the shape of the new_turtle object to "turtle"
new_turtle.color("forest green") # Changes the color of the new_turtle object to "green"

# for i in range(0,6):

#     new_turtle.right(360)
# new_turtle.forward(1000)
# new_turtle.right(180)
# new_turtle.forward(2000)

for i in range(0,4): # Creates a square with the dimensions of 100x100
    new_turtle.forward(100)
    new_turtle.left(90)








screen = Screen()
screen.exitonclick()