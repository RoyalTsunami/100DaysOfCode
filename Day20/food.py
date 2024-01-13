from turtle import Turtle
import random
from dimensions import BOX_SIZE, S_LENGTH


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("DarkSlateBlue")
        self.shapesize(0.6, 0.6)
        self.penup()
        self.speed(0)
        self.generate_food()

    def generate_food(self):
        random_x = (random.randint(0, (S_LENGTH / BOX_SIZE) - 2) * BOX_SIZE) + 10
        random_y = (random.randint(0, (S_LENGTH / BOX_SIZE) - 2) * BOX_SIZE) + 10
        self.goto(random_x, random_y)
