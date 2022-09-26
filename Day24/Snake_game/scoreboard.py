from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.get_highscore() # Reads the high score from the data.txt file and assign it to the attribute self.highscore
        self.penup()
        self.color("white")
        self.hideturtle()
        self.setposition(0, 550)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align = ALIGNMENT, font= FONT ) #  Added writing of highscore 

    # def game_over(self):
    #     self.setposition(0,0)
    #     self.write("Game over!", align= ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        
        if self.score > int(self.high_score):
            self.high_score = self.score

            with open("Day24\Snake_game\data.txt", mode = "w") as file:
                file.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    def get_highscore(self):

        with open("Day24\Snake_game\data.txt") as file:
            
            self.high_score = file.read()