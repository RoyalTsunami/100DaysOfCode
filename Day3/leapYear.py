# A year is a leap year if
# on every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400

print("Welcome to Leap Year Checker 1.1!")
# year = int(input("Which year do you want to check?\n"))
for year in range(2000, 2050):
    leapYear = False
    if not (year % 4):
        leapYear = True
        if not (year % 100):
            leapYear = False
            if not (year % 400):
                leapYear = True

    if leapYear:
        message = "is"
    else:
        message = "is not"

    print(f"The year {year} {message} a leap year.")
