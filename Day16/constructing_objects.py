# Blueprint is called the "class"
# And the instances that we generate from our class are called "objects" (are used in our code)

# Example:

# car = CarBlueprint()
# CarBlueprint() is the class where each letter of a new word is capitalised to differentiate it from functions (where each new word is separated by an underscore) in our code
# car is the objects which gets created from this car blueprint

# Example with turtle painter

import turtle

timmy = turtle.Turtle()  

# alternatively you can also just import the class

from turtle import Turtle

timmy = Turtle()

# Object attributes:

# Car example:
# car.speed # "car" is the object and "speed" is the attribute you tap into

my_screen = turtle.Screen()
print(my_screen.canvheight) # variable that is associated with an object 

# Methods:
timmy.shape("turtle") # methods that are associated with an object
timmy.color("green")
turtle.forward(100)
my_screen.exitonclick()