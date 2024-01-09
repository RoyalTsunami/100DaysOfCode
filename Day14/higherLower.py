import game_data, art, random

# score
score = 0
account1 = None
account2 = None


# functions
def space():
    print("\n")


def logo():
    print(art.logo)


def vs():
    print(art.vs)


def format(a, b):
    logo()
    print(f"Current score: {score}")
    print(f"Compare A: {compareFormat(a)}.")
    vs()
    print(f"Agaisnt B: {compareFormat(b)}.")
    print("Who has more followers?")


def compareFormat(account):
    return f"{account[0]['name']}, a {account[0]['description']}, from {account[0]['country']}"


def compareFollowers(a, b, answer):
    global account1, account2
    numA = a[0]["follower_count"]
    numB = b[0]["follower_count"]
    if numA > numB and answer == "a":
        account2 = None
        return True
    elif numB > numA and answer == "b":
        account1 = account2
        account2 = None
        return True
    else:
        account1, account2 = None, None
        return False


def generate_account():
    account = random.sample(game_data.data, 1)
    return account


def play_game():
    global score, account1, account2
    if account1 == None:
        account1 = generate_account()
    if account2 == None:
        account2 = generate_account()
    format(account1, account2)
    answer = None
    while answer != "a" and answer != "b":
        answer = input("Enter A or B only. ").lower()
    if compareFollowers(account1, account2, answer):
        print("Correct!")
        score += 1
        play_game()
    else:
        game_over()


def game_over():
    global score
    logo()
    print(f"Wrong!!! Final score: {score}")
    score = 0


# Welcome
logo()
print("Welcome to Higher or Lower!")
space()

# Game loop system
finish = False
while not finish:
    playing = input("Would you like to play the game? (y/n) ").lower()
    space()
    if playing == "y":
        play_game()
    elif playing == "n":
        finish = True
        print("Goodbye!")
        space()
        break
    else:
        print("Please only enter 'y' or 'n'.")
        space()
