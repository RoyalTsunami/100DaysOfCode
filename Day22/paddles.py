from screenformat import BOX_WIDTH, BOX_HEIGHT, PLAYER_RED_COLOR, PLAYER_YELLOW_COLOR
from turtle import Turtle

BOX_START_X = (BOX_WIDTH / 2) - 20
BOX_LIMIT_Y = BOX_HEIGHT / 2
BOX_SIZE = 20


class Paddles:
    def __init__(self) -> None:
        self.paddle_segments = []
        self.movement_speed = 20
        self.generate_paddle()

    def generate_paddle(self):
        for position in self.position:
            self.segment = Turtle()
            self.segment.shape("square")
            self.segment.color(self.colors)
            self.segment.speed(0)
            self.segment.penup()
            self.segment.goto(position[0], position[1])
            self.paddle_segments.append(self.segment)
        self.paddle_head = self.paddle_segments[1]
        self.paddle_tail = self.paddle_segments[2]

    def up(self):
        if self.paddle_head.ycor() < (BOX_LIMIT_Y - BOX_SIZE):
            for paddle_segments in self.paddle_segments:
                paddle_segments.setheading(90)
                paddle_segments.forward(self.movement_speed)

    def down(self):
        if self.paddle_tail.ycor() > (-BOX_LIMIT_Y + BOX_SIZE):
            for paddle_segments in self.paddle_segments:
                paddle_segments.setheading(270)
                paddle_segments.forward(self.movement_speed)


class Player_Red_Paddle(Paddles):
    def __init__(self) -> None:
        self.colors = PLAYER_RED_COLOR
        self.position = [
            (-BOX_START_X, 0),
            (-BOX_START_X, BOX_SIZE),
            (-BOX_START_X, -BOX_SIZE),
        ]
        self.up_pressed = False
        self.down_pressed = False
        Paddles.__init__(self)

    def move(self):
        if self.up_pressed:
            self.up()
        if self.down_pressed:
            self.down()

    def up_press(self):
        self.up_pressed = True

    def up_release(self):
        self.up_pressed = False

    def down_press(self):
        self.down_pressed = True

    def down_release(self):
        self.down_pressed = False


class Player_Yellow_Paddle(Paddles):
    def __init__(self) -> None:
        self.colors = PLAYER_YELLOW_COLOR
        self.position = [
            (BOX_START_X, 0),
            (BOX_START_X, BOX_SIZE),
            (BOX_START_X, -BOX_SIZE),
        ]
        self.up_pressed = False
        self.down_pressed = False
        Paddles.__init__(self)

    def move(self):
        if self.up_pressed:
            self.up()
        if self.down_pressed:
            self.down()

    def up_press(self):
        self.up_pressed = True

    def up_release(self):
        self.up_pressed = False

    def down_press(self):
        self.down_pressed = True

    def down_release(self):
        self.down_pressed = False
