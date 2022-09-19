from snake import Snake
import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width= 1200, height= 1200)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0) # turns off the tracer

snake = Snake()
screen.listen()

game = True

while game:

    screen.update()
    time.sleep(0.1)
    snake.move()

# Controlling the snake:

    screen.onkey(key= "Up", fun= snake.up)
    screen.onkey(key= "Down", fun = snake.down)
    screen.onkey(key= "Left", fun =snake.left)
    screen.onkey(key= "Right", fun = snake.right)
 


screen.exitonclick()