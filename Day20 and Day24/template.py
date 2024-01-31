from turtle import Turtle, Screen
from dimensions import BOX_SIZE

screen = Screen()
FONT_SCORE = ("Courier", 10, "bold")
FONT_OVER = ("Courier", 20, "bold")


# Lines
def draw_line(x_start, y_start, x_end, y_end):
    turtle = Turtle()
    turtle.hideturtle()
    turtle.color("DarkOliveGreen")
    turtle.penup()
    turtle.goto(x=x_start, y=y_start)
    turtle.pendown()
    turtle.goto(x=x_end, y=y_end)


def draw_grid(total_length, box_size):
    for i in range(int((total_length - box_size) / box_size) + 1):
        cor = (i) * box_size
        draw_line(x_start=cor, y_start=0, x_end=cor, y_end=(total_length - box_size))
        draw_line(x_start=0, y_start=cor, x_end=(total_length - box_size), y_end=cor)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, screen.screensize()[1] - BOX_SIZE)

    def update_scoreboard(self, score, highscore):
        self.clear()
        self.write(
            arg=f"Current Score: {score}   High Score: {highscore}",
            align="left",
            font=FONT_SCORE,
        )

    def game_over(self, score, highscore):
        self.clear()
        self.goto(screen.screensize()[1] / 2, screen.screensize()[1] / 2)
        if score > highscore:
            self.write(
                arg=f"Game Over! Final Score: {score}\nNew High Score: {score}",
                align="center",
                font=FONT_OVER,
            )
        else:
            self.write(
                arg=f"Game Over! Final Score: {score}\nHigh Score: {highscore}",
                align="center",
                font=FONT_OVER,
            )
