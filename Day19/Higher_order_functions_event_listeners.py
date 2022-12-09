# Turtle event listeners

# listen() allows the turtle graphics interface to start listening to keystrokes etc.

from turtle import Turtle, Screen

new_turtle = Turtle()

new_screen = Screen()

def move_forward_10():

    new_turtle.forward(10)


new_screen.listen() # screen start collecting key-strokes

new_screen.onkey(key = "space", fun = move_forward_10) # binds the function move_forward_10 to the keystroke "space", so whenever "space" is pressed the function will be triggered
# Whenever you pass a function into another function as an argument, you do not type the () at the end of the function. This is only necessary, if you want to trigger the function immediately

new_screen.exitonclick()


# Higher order function:
# - functions that are able to work with other functions 
# - basically functions that trigger other functions inside them, have them as a parameter and argument