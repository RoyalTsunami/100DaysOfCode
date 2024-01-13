from paddles import (
    BOX_START_X,
    BOX_LIMIT_Y,
    BOX_SIZE,
)
from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(
        self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True
    ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("lavender")
        self.shape("circle")
        self.penup()
        self.movement_speed = 0
        self.start_direction = ""
        self.generate_ball()
        self.move()

    def generate_ball(self):
        self.home()
        self.movement_speed = 15
        self.start_direction = random.choice(["left", "right"])
        if self.start_direction == "left":
            start_heading = random.randint(-45, 45)
        elif self.start_direction == "right":
            start_heading = random.randint(135, 225)
        self.setheading(start_heading)

    def move(self):
        self.check_if_collision()
        self.forward(int(self.movement_speed))
        if self.movement_speed <= 40:
            self.movement_speed += 0.1

    def change_angle(self):
        if self.movement_speed <= 40:
            self.movement_speed += 3
        chaos = random.randint(-30, 30)
        new_angle = -(int(self.heading()) - (180 + chaos))
        self.setheading(new_angle)
        if self.start_direction == "left":
            self.start_direction = "right"
        elif self.start_direction == "right":
            self.start_direction = "left"
        else:
            raise ValueError("Invalid start direction.")

    def check_if_collision(self):
        if self.ycor() >= (BOX_LIMIT_Y - (1.5 * BOX_SIZE)) or self.ycor() <= (
            -(BOX_LIMIT_Y - (1.5 * BOX_SIZE))
        ):
            chaos = random.randint(-20, 20)
            new_angle = -int(self.heading()) + chaos
            if self.ycor() > 0:  # top of box
                new_angle = (
                    new_angle if 180 <= new_angle < 360 else -int(self.heading())
                )
            else:  # bottom of box
                new_angle = new_angle if 0 <= new_angle < 180 else -int(self.heading())
            self.setheading(new_angle)

    def point_score(self):
        if self.xcor() < -(BOX_START_X + (2 * BOX_SIZE)):
            return "yellow scores"
        elif self.xcor() > (BOX_START_X + (2 * BOX_SIZE)):
            return "red scores"
        else:
            return False
