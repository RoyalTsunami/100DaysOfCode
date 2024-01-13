from turtle import Turtle
from dimensions import BOX_SIZE, S_LENGTH

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
CENTER = int((S_LENGTH / 2) + (BOX_SIZE / 2))
POS = [(CENTER, CENTER), (CENTER - BOX_SIZE, CENTER), (CENTER - (2 * BOX_SIZE), CENTER)]


class Snake:
    def __init__(self) -> None:
        self.shape = "square"
        self.color = "DarkOrange4"
        self.part = []
        self.initial_part()
        self.head = self.part[0]
        self.tail = self.part[-1]

    def generate_part(self, x, y):
        s_part = Turtle()
        s_part.shape(self.shape)
        s_part.color(self.color)
        s_part.penup()
        s_part.goto(x, y)
        self.part.append(s_part)

    def initial_part(self):
        for pos in POS:
            Snake.generate_part(self, pos[0], pos[1])
        self.direction = "right"

    def move(self):
        for part_num in range(len(self.part) - 1, 0, -1):
            new_x, new_y = self.part[part_num - 1].pos()
            self.part[part_num].goto(new_x, new_y)
        self.head.forward(BOX_SIZE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
