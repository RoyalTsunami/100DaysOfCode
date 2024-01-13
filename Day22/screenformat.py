from turtle import Screen, Turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.7)
BOX_WIDTH = SCREEN_WIDTH * 0.9
BOX_HEIGHT = SCREEN_HEIGHT * 0.9
BACKGROUND_COLOR = "MidnightBlue"
BOX_COLOR = "RoyalBlue4"
PLAYER_RED_COLOR = "firebrick2"
PLAYER_YELLOW_COLOR = "goldenrod"
TITLE_COLOR = "DodgerBlue"
TITLE = "PONG"
TITLE_FONT = ("ROG Fonts", int(SCREEN_WIDTH / 6), "bold")
SCORE_FONT = ("ROG Fonts", int(SCREEN_WIDTH / 10), "bold")
WIN_FONT = ("ROG Fonts", int(SCREEN_WIDTH / 20), "bold")

screen = Screen()


class Format:
    def __init__(self) -> None:
        screen.tracer(False)
        screen.bgcolor(BACKGROUND_COLOR)
        screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.box = Box()
        self.title = Title()


class Box(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.color(BOX_COLOR)
        self.pensize(10)
        self.draw_rectangle()
        self.draw_dashed_line()

    def draw_rectangle(self):
        self.penup()
        self.goto(x=(-BOX_WIDTH / 2), y=(-BOX_HEIGHT / 2))
        self.pendown()
        self.setheading(0)
        for _ in range(2):
            self.forward(BOX_WIDTH)
            self.left(90)
            self.forward(BOX_HEIGHT)
            self.left(90)

    def draw_dashed_line(self):
        self.penup()
        self.goto(x=0, y=(-BOX_HEIGHT / 2))
        self.pendown()
        self.setheading(90)
        while self.distance(x=0, y=(BOX_HEIGHT / 2)) >= 20:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)


class Title(Turtle):
    def __init__(
        self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True
    ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.hideturtle()
        self.penup()
        self.goto(0, int(-SCREEN_HEIGHT / 5))
        self.color(TITLE_COLOR)
        self.write(arg=TITLE, move=False, align="center", font=TITLE_FONT)


class Scores:
    def __init__(self) -> None:
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color(self.colors)
        self.goto(self.position)
        self.write(arg=f"{self.score}", move=False, align="center", font=SCORE_FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"{self.score}", move=False, align="center", font=SCORE_FONT)

    def check_score(self):
        if self.score == 3:
            self.goto(0, int(BOX_HEIGHT / 6))
            self.write(
                arg=f"{self.name} wins!", move=False, align="center", font=WIN_FONT
            )
            return True
        else:
            return False


class Player_Red(Turtle, Scores):
    def __init__(self) -> None:
        Turtle.__init__(self)
        self.name = "Player Red"
        self.colors = PLAYER_RED_COLOR
        self.position = (-SCREEN_WIDTH / 10), int((BOX_HEIGHT / 2) - (SCREEN_WIDTH / 8))
        Scores.__init__(self)


class Player_Yellow(Turtle, Scores):
    def __init__(self) -> None:
        Turtle.__init__(self)
        self.name = "Player Yellow"
        self.colors = PLAYER_YELLOW_COLOR
        self.position = (SCREEN_WIDTH / 10), int((BOX_HEIGHT / 2) - (SCREEN_WIDTH / 8))
        Scores.__init__(self)
