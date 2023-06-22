"""Turtle Racing Game"""
# from turtle import Turtle, Screen
# import random
#
# is_race_on = False
# screen = Screen()
# screen.setup(width=500, height=400)
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
#
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# y_positions = [-70, -40, -10, 20, 50, 80]
# all_turtles = []
#
# for turtle_index in range(6):
#     new_turtle = Turtle(shape="turtle")
#     all_turtles.append(new_turtle)
#     new_turtle.penup()
#     new_turtle.color(colors[turtle_index])
#     new_turtle.goto(-220, y_positions[turtle_index])
#
#
# if user_bet:
#     is_race_on = True
#
# while is_race_on:
#     for turtle in all_turtles:
#         random_distance = random.randint(0, 10)
#         turtle.forward(random_distance)
#         if turtle.xcor() > 230:
#             is_race_on = False
#             winning_color = turtle.pencolor()
#             if winning_color == user_bet:
#                 print(f"You've won! The {winning_color} turtle is the winner!")
#             else:
#                 print(f"You've lost. The {winning_color} turtle is the winner!")
#
# screen.exitonclick()




"""Etch a Sketch"""
# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
#
# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def turn_right():
#     tim.right(5)
#
#
# def turn_left():
#     tim.left(5)
#
#
# def clear_screen():
#     tim.home()
#     tim.clear()
#
#
# tim.speed(0)
#
# screen.listen()
# screen.onkeypress(move_forwards, "w")
# screen.onkeypress(move_backwards, "s")
# screen.onkeypress(turn_right, "d")
# screen.onkeypress(turn_left, "a")
# screen.onkey(clear_screen, "c")
# screen.exitonclick()
