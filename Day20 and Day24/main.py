from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
import template
from template import Scoreboard
from dimensions import BOX_SIZE, S_LENGTH

game_running = False
screen = Screen()
with open("Day20 and Day24\highscore.txt", mode="r") as high_score_file:
    highscore = int(high_score_file.read())


def play_game():
    global highscore
    global game_running

    # Screen
    screen.setup(width=S_LENGTH + BOX_SIZE, height=S_LENGTH + BOX_SIZE)
    screen.setworldcoordinates(llx=0, lly=0, urx=S_LENGTH, ury=S_LENGTH)
    screen.bgcolor("DarkKhaki")
    screen.title("Nokia Snake")
    screen.tracer(False)

    # Game on
    score = 0

    # Initialization
    template.draw_grid(total_length=S_LENGTH, box_size=BOX_SIZE)
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    # Controls
    screen.listen()
    screen.onkey(fun=snake.up, key="w")
    screen.onkey(fun=snake.left, key="a")
    screen.onkey(fun=snake.down, key="s")
    screen.onkey(fun=snake.right, key="d")
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.left, key="Left")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.right, key="Right")

    # Game run
    while game_running:
        scoreboard.update_scoreboard(score, highscore=highscore)
        screen.update()
        time.sleep(0.1)

        snake.move()

        # Collision with food
        if snake.head.distance(food) < 15:
            score += 1
            food.generate_food()
            new_x, new_y = snake.tail.pos()
            snake.generate_part(new_x, new_y)

        # Collision with wall
        if (
            snake.head.xcor() > (S_LENGTH - BOX_SIZE)
            or snake.head.xcor() < 0
            or snake.head.ycor() > (S_LENGTH - BOX_SIZE)
            or snake.head.ycor() < 0
        ):
            game_running = False
            scoreboard.game_over(score=score, highscore=highscore)
            if score > highscore:
                highscore = score

        # Collision with snake
        for snake_part in snake.part[1:]:
            if snake.head.distance(snake_part) < 15:
                game_running = False
                scoreboard.game_over(score=score, highscore=highscore)


while game_running == False:
    play = screen.textinput("Play Nokia Snake?", "Enter yes or no: ")
    if play == "yes":
        screen.clearscreen()
        game_running = True
        play_game()
    elif play == "no" or play == None:
        with open("Day20 and Day24\highscore.txt", mode="w") as high_score_file:
            high_score_file.write(f"{highscore}")
        break
    else:
        pass

# Exit
screen.exitonclick()
