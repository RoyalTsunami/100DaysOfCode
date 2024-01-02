import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇

choice = [rock, paper, scissors]
choices = ["rock", "paper", "scissors", "r", "p", "s"]
finish, draw, userWin, userLose = False, False, False, False
while not (finish):
    userChoice = input("Rock, paper, scissors?\n").lower()
    if userChoice == "q" or userChoice == "quit":
        finish = True
    elif userChoice in choices:
        comChoiceNum = random.randint(0, 2)
        comChoice = choice[comChoiceNum]
        comChoiceText = choices[comChoiceNum]
        if userChoice == "rock" or userChoice == "r":
            userChoice = "rock"
            userPic = rock
            if comChoice == rock:
                draw = True
            elif comChoice == paper:
                userLose = True
            elif comChoice == scissors:
                userWin = True
        elif userChoice == "paper" or userChoice == "p":
            userChoice = "paper"
            userPic = paper
            if comChoice == paper:
                draw = True
            elif comChoice == scissors:
                userLose = True
            elif comChoice == rock:
                userWin = True
        elif userChoice == "scissors" or userChoice == "s":
            userChoice = "scissors"
            userPic = scissors
            if comChoice == scissors:
                draw = True
            elif comChoice == rock:
                userLose = True
            elif comChoice == paper:
                userWin = True
        print(
            f"The computer played {comChoiceText}.\n{comChoice} \nand you played {userChoice}.\n{userPic}"
        )
        if draw:
            print("You draw!")
            draw = False
        elif userLose:
            print("You lose!")
            userLose = False
        elif userWin:
            print("You win!")
            userWin = False
    else:
        print("Please type 'rock', 'paper', 'scissors' or 'quit' only.")
