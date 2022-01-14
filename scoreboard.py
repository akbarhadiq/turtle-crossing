from turtle import Turtle
FONT = ("Courier", 15, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    # Scoreboard Object
    def __init__(self):
        super().__init__()
        self.level = 1
        # Set the color
        self.color("black")
        # hide the turtle
        self.hideturtle()
        # hide the pen, so it does not write
        self.penup()
        # make the writing go to the top of the screen
        self.goto(-240, 270)
        self.write(f"Level {self.level}", align=ALIGNMENT, font=FONT)

    # Method to update the scoreboard/Level
    def update_scoreboard(self):
        self.clear()
        self.goto(-240, 270)
        self.write(f"Level {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 270)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)

