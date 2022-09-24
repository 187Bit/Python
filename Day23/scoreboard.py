from turtle import Turtle # imports the Turtle class from the turtle module

FONT = ("Courier", 24, "normal") # Triple (3 values inside, separated by a comma), constant 

class Scoreboard(Turtle): # creating class Scoreboard that inherits from the Turtle class
    
    def __init__(self) -> None: # initialisation function
        super().__init__() # super initialisation for the inheritance of the Turtle class
        self.penup() # turtle no longer draws on screen when moving 
        self.hideturtle() # hides the turtle on the screen
        self.level = 1 # stores the level the player is currently in, starting with 1
        self.setposition(-210, 250) # sets the position of the turtle to the x-value of -210 and y-value of 250
        self.write(f"Level:{self.level}", align= "center", font= FONT) # write the string on the screen with center alignment and the font that is stored in the FONT constant

    def game_over(self):

        """Write game over in the middle of the screen."""

        self.setposition(0,0) # sets the position to the center
        self.write("Game Over", align= "center", font= FONT) # writes "Game Over" on the screen with center alignment and the font value stored in the constant FONT

    def update(self):

        """Increases the level shown on the screen by one."""

        self.level += 1 # increases the attribute level by one
        self.clear() # clear the on scree writings
        self.setposition(-210, 250) # sets the position to the x-value -210 and y-value of 250
        self.write(f"Level:{self.level}", align= "center", font= FONT) # writes the level on the screen with center alignment and the font stored in the constant FONT