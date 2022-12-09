from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.setposition(0, 550)
        self.write(f"Score: {self.score}", False, align = ALIGNMENT, font= FONT)

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, align = ALIGNMENT, font= FONT )

    def game_over(self):
        self.setposition(0,0)
        self.write("Game over!", align= ALIGNMENT, font= FONT)