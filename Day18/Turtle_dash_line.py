from turtle import Turtle, Screen # imports the Turtle and Screen class from the turtle module, much more convenient because you do not have to write turtle.Turtle etc.

new_turtle = Turtle() # Creates a new_turtle object from the Turtle class

new_turtle.shape("turtle") # Changes the shape of the new_turtle object to "turtle"
new_turtle.color("forest green") # Changes the color of the new_turtle object to "green"

for i in range(0, 16):
    new_turtle.pendown()
    new_turtle.forward(10)
    new_turtle.penup()
    new_turtle.forward(10)






screen = Screen()
screen.exitonclick()