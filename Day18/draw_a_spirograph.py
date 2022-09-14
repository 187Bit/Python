import random
from turtle import Turtle, Screen
import turtle as t

new_turtle = Turtle()

new_turtle.shape("turtle") # Changes the shape of the new_turtle object to "turtle"
new_turtle.color("forest green") # Changes the color of the new_turtle object to "green"
new_turtle.speed(1000)

def change_color():

     r = random.randint(0, 255)
     g = random.randint(0, 255)
     b = random.randint(0, 255)

     rgb_tuple = (r,g,b)

     return rgb_tuple


def draw_spirograph(size_of_gap):

    for i in range(int(360/size_of_gap)):

        random_color = change_color()
        t.colormode(255)
        new_turtle.pencolor(random_color)
        new_turtle.circle(100)
        new_turtle.setheading(new_turtle.heading() + size_of_gap)


draw_spirograph(5)
    

new_screen = Screen()
new_screen.exitonclick()