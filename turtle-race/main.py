from turtle import Turtle, Screen
import random

screen_width = 1000
screen_height = 400

is_race_on = False
screen = Screen()
screen.setup(width=screen_width, height=screen_height)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y = -120
for color in color_list:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-(screen_width/2) + 20, y=y)
    y += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > (screen_width/2) - 30:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")


screen.exitonclick()
