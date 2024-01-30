from turtle import Turtle, Screen

SCREEN_WIDTH = 800
WIDTH_COOR = SCREEN_WIDTH / 2
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.7)
HEIGHT_COOR = SCREEN_HEIGHT / 2
LANE_HEIGHT = SCREEN_HEIGHT * 0.15
BOX_SIZE = 40
BACKGROUND_COLOR = "DimGray"
SAFE_ZONE_COLOR = "OliveDrab"
LANE_COLOR = "Black"
DASH_COLOR = "SlateGray"

TITLE_COLOR = "DarkRed"
TITLE = "CROSS ROADS"
TITLE_FONT = ("Snap ITC", int(SCREEN_WIDTH / 30), "bold")
SCORE_FONT = ("Arial", int(SCREEN_WIDTH / 50), "bold")
LOSE_FONT = ("Snap ITC", int(SCREEN_WIDTH / 20), "bold")

screen = Screen()


class Format:
    def __init__(self) -> None:
        screen.tracer(False)
        screen.bgcolor(BACKGROUND_COLOR)
        screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.zone = Zone()
        screen.update()


class Zone(Turtle):
    def __init__(
        self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True
    ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.hideturtle()
        self.speed(0)
        self.pensize(10)
        self.draw_box(-WIDTH_COOR, HEIGHT_COOR, LANE_COLOR, SAFE_ZONE_COLOR)
        self.draw_box(
            -WIDTH_COOR, -HEIGHT_COOR + LANE_HEIGHT, LANE_COLOR, SAFE_ZONE_COLOR
        )
        lane_size = int(SCREEN_HEIGHT - (2 * LANE_HEIGHT))
        number_of_lanes = int(lane_size / BOX_SIZE)
        for i in range(1, number_of_lanes + 1):
            self.draw_dashed_line(HEIGHT_COOR - LANE_HEIGHT - (BOX_SIZE * i))
        self.title()

    def draw_box(self, x, y, pen_color, fill_color):
        self.penup()
        self.goto(x, y)
        self.color(pen_color, fill_color)
        self.begin_fill()
        self.pendown()
        self.setheading(0)
        for _ in range(2):
            self.forward(SCREEN_WIDTH)
            self.right(90)
            self.forward(LANE_HEIGHT)
            self.right(90)
        self.end_fill()

    def draw_dashed_line(self, y):
        self.penup()
        self.color(DASH_COLOR)
        self.goto(-WIDTH_COOR, y)
        self.pendown()
        self.setheading(0)
        while self.distance(WIDTH_COOR, y) >= 20:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def title(self):
        self.penup()
        self.goto(0, HEIGHT_COOR - (LANE_HEIGHT / 1.5))
        self.color(TITLE_COLOR)
        self.write(arg=TITLE, move=False, align="center", font=TITLE_FONT)


class Scoreboard(Turtle):
    def __init__(
        self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True
    ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.level = 0
        self.penup()
        self.hideturtle()
        self.color(TITLE_COLOR)
        self.goto(-WIDTH_COOR + 10, HEIGHT_COOR - BOX_SIZE)
        self.write(
            arg=f"Current Level: {self.level}",
            move=False,
            align="left",
            font=SCORE_FONT,
        )

    def next_level(self):
        self.level += 1
        self.clear()
        self.write(
            arg=f"Current Level: {self.level}",
            move=False,
            align="left",
            font=SCORE_FONT,
        )

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(
            arg=f"CRASH! Game over.\nFinal Level is {self.level}.",
            move=False,
            align="center",
            font=LOSE_FONT,
        )
