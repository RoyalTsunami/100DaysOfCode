# Program should print numbers 1 to 100 in turn
# When the number is divisible by 3 then
# instead of the number, it should print "Fizz"
# When the number is divisible by 5,
# it should print "Buzz"
# If divisible by both 3 and 5, print "FizzBuzz"

for num in range(1, 101):
    if not (num % 3) and not (num % 5):
        print("FizzBuzz")
    elif not (num % 3):
        print("Fizz")
    elif not (num % 5):
        print("Buzz")
    else:
        print(num)
