from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score}     {self.r_score}", move=False, align=ALIGNMENT, font=FONT)

    def l_increase_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_increase_score(self):
        self.r_score += 1
        self.update_scoreboard()
