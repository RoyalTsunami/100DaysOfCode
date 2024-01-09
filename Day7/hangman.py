import random, wordList, picture

print("Welcome to Hangman!")
print("//////////////////////////////////////////")
print(picture.logo)

answer = random.choice(wordList.word_list)
answerList = list(answer)
chances = 6

guessList = []
for i in answerList:
    guessList.append("_")

guessedLetters = []

while (guessList != answerList) and chances:
    print("//////////////////////////////////////////")
    print(picture.stages[chances])
    print(guessList)
    print(f"You have {chances} chance left to guess.")
    guessPlayer = input("Guess a letter: ").lower()
    if guessPlayer == "stop":
        print("//////////////////////////////////////////")
        print("Game is over.")
        break
    elif guessPlayer not in wordList.alphabet_list:
        print("//////////////////////////////////////////")
        print("Please enter only a letter.")
    elif guessPlayer in guessedLetters:
        print("//////////////////////////////////////////")
        print("You have guessed this letter previously.")
    elif guessPlayer in answerList:
        print("//////////////////////////////////////////")
        print("You have guessed correctly.")
        guessedLetters.append(guessPlayer)
        for letter in range(len(answerList)):
            if answerList[letter] == guessPlayer:
                guessList[letter] = guessPlayer
    else:
        print("//////////////////////////////////////////")
        print("You have guessed wrongly.")
        guessedLetters.append(guessPlayer)
        chances -= 1

if guessList == answerList:
    print(picture.stages[chances])
    triesTaken = len(guessedLetters)
    print(
        f"Congratz! The word is {answer} and it took you {triesTaken} guesses to get it right!"
    )
elif not (chances):
    print(picture.stages[chances])
    print("You died. Game over.")
