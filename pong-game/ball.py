from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")

    def move(self):
        new_x = self.xcor() + 8
        new_y = self.ycor() + 6
        self.goto(new_x, new_y)