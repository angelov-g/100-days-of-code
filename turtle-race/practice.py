from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_clockwise():
    tim.right(10)


def turn_counterclocwise():
    tim.left(10)


def reset():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_counterclocwise)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=reset)

screen.exitonclick()
