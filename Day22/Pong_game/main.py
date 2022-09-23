from turtle import Screen
from paddle_single import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

game = True

screen = Screen()
screen.setup(width= 1600, height= 1200)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

right_paddle = Paddle((700, 0))
left_paddle = Paddle((-700, 0))
ball = Ball()
scoreboard = Scoreboard()


while game:

    screen.listen()
    screen.update()
    time.sleep(0.01)


    # Controls for the left_paddle

    screen.onkeypress(key = "w", fun = left_paddle.move_up) # Do not include () after the function otherwise it will call the function without a keypress
    screen.onkeypress(key = "s", fun = left_paddle.move_down)

    # Controls for the right_paddle

    screen.onkeypress(key = "Up", fun = right_paddle.move_up) # Do not include () after the function otherwise it will call the function without a keypress
    screen.onkeypress(key = "Down", fun = right_paddle.move_down)

    # Controls the movement of the ball:
    ball.move()

    # Detect collision with top and bottom wall:

    if ball.ycor() > 590 or ball.ycor() < -590:
        ball.bounce_y()

    # Detect collision with left and right paddle:
    
    if ball.distance(right_paddle) < 50 and ball.xcor() > 680 or ball.distance(left_paddle) < 50 and ball.xcor() < -680:
        ball.bounce_x()
        ball.change_speed()
        
     # Detect when a paddle has missed the ball:
    if ball.xcor() > 800:
        ball.reset_position()
        scoreboard.l_score += 1
        scoreboard.update()


    if ball.xcor() < -800:
        ball.reset_position()
        scoreboard.r_score += 1
        scoreboard.update()
        

    
screen.exitonclick()