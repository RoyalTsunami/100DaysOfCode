from turtle import Turtle, Screen
import random

# Screen Setup
screen_width = 500
screen_height = 400

screen = Screen()
screen.setworldcoordinates(llx=0, lly=0, urx=screen_width, ury=screen_height)

# Bet
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win?\n(red/orange/yellow/green/blue/violet/purple): ",
)
is_race_on = True

# Race Lines
screen.tracer(False)

start_line_x = 10
end_line_x = screen_width - (start_line_x * 2)


def race_lines(x_line):
    race_line_turtle = Turtle()
    race_line_turtle.speed(0)
    race_line_turtle.hideturtle()
    race_line_turtle.penup()
    race_line_turtle.goto(x=x_line, y=0)
    race_line_turtle.pendown()
    race_line_turtle.goto(x=x_line, y=screen_height)


race_lines(x_line=start_line_x)
race_lines(x_line=end_line_x)

# Turtle
colors = ["red", "orange", "yellow", "green", "blue", "violet", "purple"]
race_turtle_list = []
for i in range(len(colors)):
    race_turtle = Turtle()
    race_turtle.color(colors[i])
    race_turtle.shape("turtle")
    start_y = (i + 1) * 50
    race_turtle.penup()
    race_turtle.goto(x=start_line_x, y=start_y)
    race_turtle_list.append(race_turtle)

screen.tracer(True)
# Race
while is_race_on:
    for race_turtle in race_turtle_list:
        rand_distance = random.randint(0, 20)
        race_turtle.forward(rand_distance)
        race_turtle_x_pos = race_turtle.pos()[0]
        if race_turtle_x_pos >= end_line_x:
            winner = race_turtle.color()[0]
            is_race_on = False

# Winner declaration
print(f"The winner is the {winner} turtle!")

if user_bet == winner:
    print(f"You bet on {user_bet} and guessed correctly! Congratz.")
else:
    print(f"You bet on {user_bet} and got it wrong! Better luck next time.")

# Exit
screen.exitonclick()
