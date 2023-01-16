# import colorgram
#
# extracted_colors = colorgram.extract('image.jpg', 10)
# formatted_colors = []
# for current_color in extracted_colors:
#     red = current_color.rgb.r
#     green = current_color.rgb.g
#     blue = current_color.rgb.b
#     color_tuple = (red, green, blue)
#     formatted_colors.append(color_tuple)
# print(formatted_colors)
import turtle
import random

turtle.colormode(255)

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53),
              (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48)]


def damien_hirst(grid_x, grid_y, grid_spacing, dot_size):
    x_length = (grid_x * grid_spacing) - grid_spacing
    y_length = (grid_y * grid_spacing) - grid_spacing

    pos_x = int(x_length/2)
    neg_x = int(-x_length/2)
    pos_y = int(y_length/2)
    neg_y = int(-y_length/2)

    damien = turtle.Turtle()
    damien.hideturtle()
    damien.speed(0)
    damien.pu()

    for y_pos in range(neg_y, pos_y + 1, grid_spacing):
        for x_pos in range(neg_x, pos_x + 1, grid_spacing):
            damien_color = random.choice(color_list)
            damien.goto(x_pos, y_pos)
            damien.dot(dot_size, damien_color)


damien_hirst(10, 10, 50, 30)

my_screen = turtle.Screen()
my_screen.exitonclick()
