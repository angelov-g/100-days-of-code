import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
timmy_the_turtle = Turtle()
colour_palette = ["medium slate blue", "slate blue", "dark slate blue", "medium orchid", "orchid", "dark orchid"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# # Drawing a square
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# # Drawing a dashed line
# for _ in range(10):
#     timmy_the_turtle.forward(5)
#     timmy_the_turtle.pu()
#     timmy_the_turtle.forward(5)
#     timmy_the_turtle.pd()

# # Drawing different shapes
# colours = ["red", "green", "blue", "black", "pink", "orange", "yellow", "brown"]
# for n_sides in range(3, 11):
#     timmy_the_turtle.color(random.choice(colours))
#     angle = 360 / n_sides
#     for _ in range(n_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)

# # Random walk
#
# direction = [0, 90, 180, 270]
# timmy_the_turtle.width(10)
# timmy_the_turtle.speed(0)
# for _ in range(1000):
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.forward(20)
#     timmy_the_turtle.setheading(random.choice(direction))

# Spirograph
timmy_the_turtle.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy_the_turtle.color(random.choice(colour_palette))
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)


draw_spirograph(6)











screen = Screen()
screen.exitonclick()
