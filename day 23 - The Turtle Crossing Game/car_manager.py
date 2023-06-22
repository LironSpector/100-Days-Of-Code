from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 4) == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT



# class CarManager(Turtle):
#     def __init__(self):
#         super().__init__()
#         # self.create_car()
#
#         self.shape("square")
#         self.color(random.choice(COLORS))
#         self.penup()
#         self.setheading(180)
#         self.shapesize(stretch_wid=1, stretch_len=2)
#         x_position = 320
#         y_position = random.randint(-250, 250)
#         self.goto(x_position, y_position)

