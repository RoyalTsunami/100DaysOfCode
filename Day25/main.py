import turtle, pandas

screen = turtle.Screen()
screen.title("Guess U.S. States!")

image = "Day25\\blank_states_img.gif"
screen.addshape(image)
map = turtle.shape(image)
screen.tracer(False)

data = pandas.read_csv("Day25\\50_states.csv")

# Ask for player input
finish = False
correct = 0

while not finish:
    if correct == 0:
        title_prompt = "Guess A State"
    else:
        title_prompt = f"{correct}/50 States Correct"
    player_answer = screen.textinput(
        title=title_prompt, prompt="Enter a state's name: "
    )
    if player_answer == None:
        finish = True
        break
    else:
        for state in data.state:
            if state == player_answer.title():
                state_data = data[data.state == state]
                data = data.drop(state_data.index)
                x_cor = state_data.x.values[0]
                y_cor = state_data.y.values[0]
                coor = turtle.Turtle()
                coor.penup()
                coor.hideturtle()
                coor.goto(x=x_cor, y=y_cor)
                coor.write(
                    arg=state,
                    align="center",
                    font=["Arial", 10, "bold"],
                )
                correct += 1
        if correct == 50:
            finish = True
            win = turtle.Turtle()
            win.hideturtle()
            win.write(
                arg="You've guessed all the states!",
                align="center",
                font=["Arial", 30, "bold"],
            )
        screen.update()


turtle.mainloop()
