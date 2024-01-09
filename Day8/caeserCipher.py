import art

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def cipher(text, shift, direction):
    textList = list(text)
    newText = ""
    if direction == "decode":
        shift *= -1
    for i in range(len(textList)):
        if textList[i] in alphabet:
            for originalLetter in alphabet:
                if textList[i] == originalLetter:
                    originalIndex = alphabet.index(textList[i])
                    break
            newIndex = (originalIndex + shift) % len(alphabet)
            newText += alphabet[newIndex]
        else:
            newText += textList[i]
    print(f"The new message is {newText}.\n")


print(art.logo)
print("Welcome to Caesar Cipher Machine v1.")
finish = False
while not finish:
    play = input("Type 'start' to begin or 'stop' to quit the program.\n").lower()
    if play == "start":
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n"
        ).lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        cipher(text, shift, direction)
    elif play == "stop":
        print("Bye!")
        finish = True
    else:
        print("Please enter 'start' or 'stop'.")
