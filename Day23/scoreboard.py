from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.setposition(-210, 250)
        self.write(f"Level:{self.level}", align= "center", font= FONT)

    def game_over(self):
        self.setposition(0,0)
        self.write("Game Over", align= "center", font= FONT)

    def update(self):
        self.level += 1
        self.clear()
        self.setposition(-210, 250)
        self.write(f"Level:{self.level}", align= "center", font= FONT)