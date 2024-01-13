from turtle import Screen
from screenformat import Format, Player_Red, Player_Yellow
import time
from paddles import Player_Red_Paddle, Player_Yellow_Paddle
from ball import Ball

screen = Screen()
screen.tracer(False)


# Function to check if ball hits paddle
def check_ball_hits_paddle(ball, paddle, direction):
    for segment in paddle.paddle_segments:
        if ball.distance(segment) < 30 and ball.start_direction == direction:
            ball.change_angle()


def play_game():
    # Init
    game_is_running = True
    Format()
    player_red_score = Player_Red()
    player_yellow_score = Player_Yellow()
    red_paddle = Player_Red_Paddle()
    yellow_paddle = Player_Yellow_Paddle()
    ball = Ball()
    screen.update()
    time.sleep(0.5)

    # Controls
    screen.listen()
    screen.onkeypress(fun=red_paddle.up_press, key="w")
    screen.onkeyrelease(fun=red_paddle.up_release, key="w")
    screen.onkeypress(fun=red_paddle.down_press, key="s")
    screen.onkeyrelease(fun=red_paddle.down_release, key="s")
    screen.onkeypress(fun=yellow_paddle.up_press, key="Up")
    screen.onkeyrelease(fun=yellow_paddle.up_release, key="Up")
    screen.onkeypress(fun=yellow_paddle.down_press, key="Down")
    screen.onkeyrelease(fun=yellow_paddle.down_release, key="Down")

    # Dictionary for scores
    scores = {"red scores": player_red_score, "yellow scores": player_yellow_score}

    while game_is_running:
        red_paddle.move()
        yellow_paddle.move()
        ball.move()
        screen.update()
        time.sleep(0.1)

        # Check if ball hits paddles
        check_ball_hits_paddle(ball, red_paddle, "right")
        check_ball_hits_paddle(ball, yellow_paddle, "left")

        # Check if ball goes past the paddle
        scorer = ball.point_score()
        if scorer in scores:
            scores[scorer].update_score()
            ball.generate_ball()

        # Check if game is over
        if any(score.check_score() for score in scores.values()):
            game_is_running = False
            break


finish = False
Format()
screen.update()

while not finish:
    play = screen.textinput(title="Play?", prompt="Enter yes or no:")
    if play == "yes":
        screen.clearscreen()
        play_game()
    elif play == "no" or play == None:
        finish = True
        break

# Exit
screen.exitonclick()
