# 1. Create a greeting for your program.
print(
    "Hello! Welcome to Band Name Generator where you can generate \n"
    "your own personalized band name with just a click of a button!"
)
# 2. Ask the user for the city that they grew up in.
city = input("Which city did you grow up in? \n")
# 3. Ask the user for the name of a pet.
pet = input("What is the name of your pet? \n")
# 4. Combine the name of their city and pet and show them their band name.
bandName = city + " " + pet
# 5. Make sure the input cursor shows on a new line:
print("This is your personalized band name! " + bandName)
