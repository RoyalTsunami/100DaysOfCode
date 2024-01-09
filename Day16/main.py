from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

power = True
menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

while power:
    menu = Menu()
    choice = input(f"\nWhat would you like to have?\n({menu.get_items()})")
    if choice == "quit":
        print("Power Off.")
        power = False
        break
    elif choice == "report":
        coffeemaker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink) and moneymachine.make_payment(
            drink.cost
        ):
            coffeemaker.make_coffee(drink)
