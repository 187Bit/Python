from turtle import Turtle, Screen # imports the Turtle and Screen class from the turtle module, much more convenient because you do not have to write turtle.Turtle etc.
import random
import turtle as t

new_turtle = Turtle() # Creates a new_turtle object from the Turtle class

new_turtle.shape("turtle") # Changes the shape of the new_turtle object to "turtle"
new_turtle.color("forest green") # Changes the color of the new_turtle object to "green"

new_turtle.speed(1000)

def change_color():

    number_list = []

    for i in range(0,3):
        new_number = random.randint(0,255)
        number_list.append(new_number)

    return number_list

def random_number():
    angles = [0, 90, 180, 270]
    random_angle = random.choice(angles)
    print(random_angle)
    return random_angle

for i in range(0,200):

    new_turtle.pensize(20)
    returned = change_color()
    t.colormode(255)
    new_turtle.pencolor((returned[0],returned[1],returned[2]))

    random_angle = random_number()

    new_turtle.setheading(random_angle)
    new_turtle.forward(50)



screen = Screen()
screen.exitonclick()