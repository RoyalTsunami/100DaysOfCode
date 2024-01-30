from turtle import Turtle
from screen_format import (
    WIDTH_COOR,
    BOX_SIZE,
    SCREEN_HEIGHT,
    LANE_HEIGHT,
    HEIGHT_COOR,
)
import random

color_range = [
    "darkred",
    "red",
    "lightpink",
    "pink",
    "salmon",
    "darkorange",
    "orange",
    "darkblue",
    "blue",
    "lightblue",
    "skyblue",
    "steelblue",
]
y_cor = []
lane_size = int(SCREEN_HEIGHT - (2 * LANE_HEIGHT))
number_of_lanes = int(lane_size / BOX_SIZE)
for i in range(1, number_of_lanes + 1):
    y = HEIGHT_COOR - LANE_HEIGHT - (BOX_SIZE * i) + (BOX_SIZE / 2)
    y_cor.append(y)


class Car:
    def __init__(self) -> None:
        self.shape = "square"
        self.car_list = []

    def generate_car(self, current_level):
        car_limit = 10 + (current_level * 2)
        if len(self.car_list) < car_limit:
            car = Turtle()
            car.shape(self.shape)
            car.shapesize(1, 2)
            car.speed(0)
            car.penup()
            car.setheading(180)
            color = random.choice(color_range)
            car.color(color)
            y = random.choice(y_cor)
            x = random.randint(-WIDTH_COOR + BOX_SIZE, WIDTH_COOR + BOX_SIZE)
            car.goto(x, y)
            self.car_list.append(car)

    def move_car(self, current_level):
        for car in self.car_list:
            y = car.ycor()
            movement_speed = int(1 + current_level * 0.01)
            if car.distance(-WIDTH_COOR, y) <= 5:
                new_y = random.choice(y_cor)
                car.goto(WIDTH_COOR + BOX_SIZE, new_y)
            car.forward(movement_speed)

    def check_collision(self, player):
        for car in self.car_list:
            if car.distance(player) <= 20:
                return True
