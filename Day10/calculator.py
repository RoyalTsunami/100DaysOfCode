import art

print(art.logo)
print("Welcome to your handy Calculator!")
firstNum = None
finish = False


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

while not finish:
    if firstNum is None:
        firstNum = float(input("What's the first number?: "))
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    secondNum = float(input("What's the next number?: "))
    result = 0
    calculatorFunction = operations.get(operation)
    if calculatorFunction in operations.values():
        result = calculatorFunction(firstNum, secondNum)
    else:
        print("Invalid operation")
    print(f"{firstNum} {operation} {secondNum} = {result}")
    choice = input(
        f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
    )
    if choice == "stop":
        finish = True
        print("Goodbye!")
    elif choice == "n":
        firstNum = None
        print("Starting new calculation...")
    else:
        firstNum = result
