from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.title("PONG")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle()

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
