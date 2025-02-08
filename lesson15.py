#while loop = executes some codes while some conditions remains true


name = input("Please enter your name: ")

while name == "":   # user is reprompted to enter their name if they leave blank.
    print("You did not enter your name")
    name = input("Please enter your name: ")

print(f"Hello {name}")

age = int(input("Please enter your age: "))

while age < 0: # the user is prompted to reenter their age if they enter a -ve integer
    print("Your age cannot be a negative.")
    age = int(input("Please enter your age: "))

print(f"You are {age} years old")


num = int(input("Please enter any number between 100 and 1000: "))

while num < 100 or num > 1000:
    print("Your number does not fall between the provided range")
    num = int(input("Please enter any number between 100 and 1000: "))
print(f"{num} is correct")