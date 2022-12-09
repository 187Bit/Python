from snake import Snake
import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width= 1200, height= 1200)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0) # turns off the tracer

snake = Snake()
screen.listen()
food = Food()
scoreboard = Scoreboard()

game = True


while game:

    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food:

    if snake.head.distance(food) < 15: # checks if the distance between the snake head and the food object (distance in pixels) is lower than 15 pixels
        food.refresh()
        snake.extend()
         # Creating the scoreboard (shows the score of the amount of food that the snake ate)
        scoreboard.update_scoreboard()

    # Detect collision with wall:

    if snake.head.xcor() > 590 or snake.head.xcor() < -590 or snake.head.ycor() > 590 or snake.head.ycor() < -590:
        game = False
        scoreboard.game_over()

    # Füüd

    # Detect collision with tail:

    # for segment in snake.all_squares:
    #     if segment == snake.head: # checks if the current segment in the for loop is equal to the snake head
    #         pass # if condition above is True, will pass the elif statement
    
    for segment in snake.all_squares[1:]:
        if snake.head.distance(segment) < 10:
            game = False
            scoreboard.game_over()
   
# Controlling the snake:

    screen.onkey(key= "Up", fun= snake.up)
    screen.onkey(key= "Down", fun = snake.down)
    screen.onkey(key= "Left", fun =snake.left)
    screen.onkey(key= "Right", fun = snake.right)
 
screen.exitonclick()