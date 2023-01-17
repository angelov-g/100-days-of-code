from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.hideturtle()

    def initialize(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.initialize()
