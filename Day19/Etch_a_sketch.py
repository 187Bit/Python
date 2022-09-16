from turtle import Turtle, Screen

new_turtle = Turtle()
new_screen = Screen()
new_screen.listen()

def turtle_forwards():
    new_turtle.forward(10)

def turtle_backwards():
    new_turtle.backward(10)

def turtle_counter_clockwise():
    new_turtle.left(10)

def turtle_clockwise():
    new_turtle.right(10)

def turtle_clear():

    new_turtle.reset()


new_screen.onkey(key = "w", fun = turtle_forwards)
new_screen.onkey(key = "s", fun = turtle_backwards)
new_screen.onkey(key = "a", fun = turtle_counter_clockwise)
new_screen.onkey(key = "d", fun = turtle_clockwise)
new_screen.onkey(key = "c", fun = turtle_clear)


new_screen.exitonclick()