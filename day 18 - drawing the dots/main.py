import random
import turtle
from turtle import Turtle, Screen

color_list = [(208, 160, 101), (150, 75, 37), (231, 213, 97), (132, 34, 21), (191, 156, 15), (87, 33, 21),
              (238, 174, 153), (21, 57, 80), (41, 117, 63), (31, 93, 135), (196, 98, 88), (2, 81, 115), (10, 99, 77),
              (194, 163, 165), (109, 159, 185), (73, 76, 40), (179, 209, 168), (106, 140, 129), (37, 27, 35),
              (78, 153, 168), (46, 50, 47), (134, 163, 150), (234, 178, 180), (2, 72, 136), (125, 64, 66), (118, 36, 39)]

turtle.colormode(255)
timmy = Turtle()
timmy.speed(0)
timmy.hideturtle()
timmy.penup()
timmy.goto(-200, -200)


x_position = timmy.position()[0]
y_position = timmy.position()[1]

for dot_count in range(100):
    if dot_count % 10 == 0 and dot_count != 0:
        y_position += 50
        timmy.goto(x_position, y_position)

    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)


screen = Screen()
screen.exitonclick()







"""how I created the color_list: """
# import colorgram
# from image import image.jpg
#
# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)



# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for color in colors:
#     rgb_colors.append(color.rgb[0:3])
#
# print(rgb_colors)
