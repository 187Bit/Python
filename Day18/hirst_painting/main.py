# import colorgram

# colors = colorgram.extract(r'C:\Users\PVTJL\OneDrive\Work-Education\Coding\Development\Languages\Python\Day18\hirst_painting\image.jpg', 30) #needs a raw string instead of a normal string, r("string")

# color_list = [] 

# for i in range(0, len(colors)):

#     current_color = colors[i] # assing one color object at the position "i" to the variable current_color
#     color_tuple = (current_color.rgb[0], current_color.rgb[1], current_color.rgb[2]) # creates a new tuple called color_tuple and assign the rgb values stored in the variable current color at each postion
#     color_list.append(color_tuple) # appends the color_tuple to the color_list list

from turtle import Turtle, Screen
import random 
import turtle as t

all_colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

def get_color(color_list):

    random_color = random.choice(color_list)

    return random_color

def draw_painting():
    
    t.colormode(255)
    new_turtle = Turtle()
    new_turtle.color("forest green")
    new_turtle.hideturtle()
    new_turtle.penup()
    # new_turtle.setposition(-400, -400)
    new_turtle.setheading(225)
    new_turtle.forward(300)
    new_turtle.setheading(0)
    new_turtle.pendown()

    for i in range(1,101):

        color = get_color(all_colors)
        new_turtle.dot(20, color)
        new_turtle.penup()
        new_turtle.forward(50)
        new_turtle.pendown()

        if int(i % 10) == 0:
            current_position = new_turtle.position()
            new_turtle.penup()
            new_turtle.setposition(current_position[0] - 500, current_position[1] + 50)
            new_turtle.pendown()


    new_screen = Screen()
    new_screen.exitonclick()

draw_painting()