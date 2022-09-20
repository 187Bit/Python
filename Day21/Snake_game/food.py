from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5) # shrinks down the size of the circle by 50% or half
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-580, 580)
        random_y = random.randint(-580, 580)
        self.setposition(random_x, random_y)

    def refresh(self): # Do not forget the "self"!
        random_x = random.randint(-580, 580)
        random_y = random.randint(-580, 580)
        self.setposition(random_x, random_y)