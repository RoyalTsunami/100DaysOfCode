from screen_format import HEIGHT_COOR, BOX_SIZE, LANE_HEIGHT
from turtle import Turtle

TURTLE_COLOR = "NavajoWhite"
TURTLE_SPEED = int(BOX_SIZE / 2)
TURTLE_START_POS = 0, -HEIGHT_COOR + BOX_SIZE


class Player(Turtle):
    def __init__(
        self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True
    ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color(TURTLE_COLOR)
        self.shapesize(1.5, 1.5)
        self.speed(0)
        self.goto(TURTLE_START_POS)
        self.shape("turtle")
        self.setheading(90)

    def player_move(self):
        self.forward(TURTLE_SPEED)

    def check_finish_line(self):
        if self.distance(0, HEIGHT_COOR - LANE_HEIGHT / 2) <= 20:
            self.goto(TURTLE_START_POS)
            return True
        else:
            return False
