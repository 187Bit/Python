from turtle import Turtle

class Paddles(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.paddle_list = []
        self.create_paddle()
        self.right_paddle = self.paddle_list[0]
        self.left_paddle = self.paddle_list[1]

    def create_paddle(self):

        for i in range(0,2):

            paddle = Turtle("square")
            paddle.penup()
            paddle.color("white")
            paddle.turtlesize(stretch_wid= 5, stretch_len = 1)
            self.paddle_list.append(paddle)

    def set_position_right(self):
        self.right_paddle.setposition(700, 0)

    def set_position_left(self):
        self.left_paddle.setposition(-700, 0)
    	
    def move_up(self):
        y = self.right_paddle.ycor() + 20
        self.right_paddle.sety(y)
        
    def move_down(self):
        y = self.right_paddle.ycor() - 20
        self.right_paddle.sety(y)