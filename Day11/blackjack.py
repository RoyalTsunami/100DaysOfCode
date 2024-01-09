import art, random

# Welcome
print(art.logo)
print("Welcome to 'Investing' 2.0!")

# Cards
cards = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}


def add_card(person):
    card_value = random.choice(list(cards.values()))
    while 11 in person and (sum(person) + card_value) > 21:
        ace = person.index(11)
        person[ace] = 1
    return person.append(card_value)


# Game start loop
finish = False
while not finish:
    game_start = input("Do you want to play a game of BlackJack?\n(y/n) ").lower()
    if game_start == "n":
        finish = True
        break
    elif game_start != "y":
        print("Please enter 'y' or 'n'.")
        continue

    dealer_cards = []
    dealer_card_sum = 0
    while dealer_card_sum < 17:
        add_card(dealer_cards)
        dealer_card_sum = sum(dealer_cards)
    print(f"\nDealer's first card is {dealer_cards[0]}.")
    print(f"Debug: Dealer's cards are {dealer_cards}")

    player_cards = []
    player_card_sum = 0
    for i in range(2):
        add_card(player_cards)
        player_card_sum = sum(player_cards)
    print(
        f"\nYour cards' values: [{player_cards}]"
        + f"\nCurrent score: {player_card_sum}\n"
    )
    hit = None
    while player_card_sum <= 21 and hit != "n" and len(player_cards) < 5:
        hit = input("Would you like to draw another card?\n(y/n) ")
        if hit == "n":
            break
        elif hit == "y":
            add_card(player_cards)
            player_card_sum = sum(player_cards)
            print(
                f"\nYour cards' values: [{player_cards}]"
                + f"\nCurrent score: {player_card_sum}\n"
            )

    print(
        f"\nDealer cards' values: {dealer_cards}"
        + f"\nDealer's score: {dealer_card_sum}\n"
        + f"\nYour cards' values: {player_cards}"
        + f"\nFinal score: {player_card_sum}\n"
    )
    if player_card_sum > 21:
        print("Busted! Your cards went over 21! You lose!")
    elif dealer_card_sum > 21:
        print("The dealer busted! You win!")
    elif len(player_cards) == 5:
        print("You drew five cards and did not exceed 21! You win!")
    elif hit == "n":
        if dealer_card_sum > player_card_sum:
            print("You lose!")
        elif player_card_sum > dealer_card_sum:
            print("You win!")
        elif player_card_sum == dealer_card_sum:
            print("Draw!")
