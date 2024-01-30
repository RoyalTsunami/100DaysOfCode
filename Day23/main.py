from screen_format import Format, Scoreboard, screen
import time
from player import Player
from car_manager import Car


def game_start():
    game_running = True
    score = Scoreboard()
    player = Player()
    car = Car()
    screen.update()
    time.sleep(0.5)

    screen.listen()
    screen.onkey(fun=player.player_move, key="space")
    while game_running:
        if player.check_finish_line():
            score.next_level()
        car.generate_car(score.level)
        car.move_car(score.level)
        if car.check_collision(player):
            game_running = False
            score.game_over()
            screen.update()
            time.sleep(2)

        screen.update()


finish = False

while not finish:
    screen.clearscreen()
    player_choice = screen.textinput(
        title="Play Cross Roads?", prompt="Enter yes or no"
    )
    if player_choice == None:
        finish = True
        break
    elif player_choice.lower() == "yes":
        format = Format()
        game_start()
    elif player_choice.lower() == "no":
        finish = True
