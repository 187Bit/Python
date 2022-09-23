from turtle import Turtle

# MOVESPEED = 2.5

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.MOVESPEED = 2.5
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_direction = self.MOVESPEED
        self.y_direction = self.MOVESPEED
        self.amount_of_hits = []
        self.value = 0
        
        

    def move(self):
        # You can also create new variables for the new position like:
        # new_x = self.xcor() + MOVESPEED
        # new_y = self.ycor() + MOVESPEED
        # self.setposition(new_x, new_y)
        
        

        self.setposition(self.xcor() + self.x_direction, self.ycor()+self.y_direction) # moves the ball 10 pixels to the right on both the x and y axis from the current position
        
    def bounce_y(self):
        self.y_direction *= -1

    def bounce_x(self):
        self.x_direction *= -1
        
    def reset_position(self):
        if self.xcor() > 800:
            self.home()
            self.bounce_x()
        
        if self.xcor() < -800:
            self.home()
            self.bounce_x()
        

        for i in self.amount_of_hits:
            print("executed")
            print(self.x_direction)
            # self.value = self.amount_of_hits * 1.2
            # print(self.value)
            self.x_direction /= 1.2
            self.y_direction /= 1.2
    
        self.amount_of_hits = []

    def change_speed(self):
        print(f"First: {self.x_direction}")
        self.x_direction *= 1.2
        number = round(self.x_direction, 2)
        self.x_direction = number
        print(f"Second: {self.x_direction}")
        self.amount_of_hits.append(1)