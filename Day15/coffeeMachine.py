import ingredients

# Asks user for input

power = True
menuOptions = list(ingredients.MENU.keys())
profit = 0


def order():
    menu = ""
    for items in range(len(menuOptions)):
        menu += f"{items}: {menuOptions[items]} (${ingredients.MENU[menuOptions[items]]['cost']})\n"
    moreOptions = f"{len(menuOptions)}: report\n{len(menuOptions)+1}: quit"
    print(f"\nWhat would you like?\n{menu}{moreOptions}")
    choice = int(input("Enter the corresponding number: "))
    if choice == len(menuOptions):
        report()
        return
    elif choice == (len(menuOptions) + 1):
        quit()
        return
    elif choice in list(range(len(menuOptions))):
        drink = menuOptions[choice]
        resource_sufficient(drink)


def quit():
    global power
    power = False
    print("Power off.")
    return


def report():
    print("")
    for resource, amount in ingredients.resources.items():
        if resource == "water" or resource == "milk":
            measurement = "ml"
        elif resource == "coffee":
            measurement = "g"
        print(f"{resource.title()}: {amount}{measurement}")
    print(f"Money: ${profit}")
    return


def resource_sufficient(drink):
    enough = True
    for item in ingredients.MENU[drink]["ingredients"].items():
        resource, amount = item
        if ingredients.resources[resource] < amount:
            print(f"Sorry, there is not enough {resource}.")
            enough = False
    if enough:
        return payment(drink)
    else:
        return


def payment(drink):
    global profit
    quarters = int(input("How many quarters ($0.25)?: ")) * 0.25
    dimes = int(input("How many dimes? ($0.10): ")) * 0.10
    nickles = int(input("How many nickles? ($0.05): ")) * 0.05
    pennies = int(input("How many pennies? ($0.01): ")) * 0.01
    payment_total = float(
        "{:.2f}".format(round(quarters + dimes + nickles + pennies, 2))
    )
    cost = float(ingredients.MENU[drink]["cost"])
    if payment_total > cost:
        change = "{:.2f}".format(round(payment_total - cost, 2))
        print(f"Here is ${change} in change.")
        profit += cost
        return make_drink(drink)
    else:
        deficit = "{:.2f}".format(round(cost - payment_total, 2))
        print(
            f"Sorry, that is not enough money. You need ${deficit} more. Money refunded."
        )


def make_drink(drink):
    for item in ingredients.MENU[drink]["ingredients"].items():
        resource, amount = item
        ingredients.resources[resource] = ingredients.resources[resource] - amount
    print(f"Here is your {drink}: Enjoy!")


while power:
    order()
