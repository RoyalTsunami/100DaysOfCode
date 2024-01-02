print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

move = input(
    "You are at the cross road.\nWould you like to go left or right?\n"
).lower()
if move == "left":
    move2 = input("You arrive at a lake.\nWould you like to swim or wait.\n").lower()
    if move2 == "wait":
        move3 = input(
            "You see three colored doors.\nDo you want to go to the red, blue or yellow door?\n"
        ).lower()
        if move3 == "red":
            print("Flames engulfed you as you touched the door handle. Game Over.")
        elif move3 == "blue":
            print(
                "You walk pass the door and was ambushed by hungry wolves. Game Over."
            )
        elif move3 == "yellow":
            print("You found the treasure. You win!")
        else:
            print("What are you doing? A tree fell on top of you. Game Over.")
    elif move2 == "swim":
        print(
            "A tentacle wrap itself around your legs and dragged you under. Game Over."
        )
    else:
        print("What are you doing? You slipped into the lake and drowned. Game Over.")
elif move == "right":
    print("You fell down a cliff. Game Over.")
else:
    print("What are you doing? You stumbled and fell into a hole. Game Over.")
