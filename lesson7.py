# python weight converter:
weight = float(input("Enter your weight papi: "))
unit = input("Is your weight in Kg or pounds: ")


if unit == "kg":
    print(f"Your weight is {round(weight * 2.204623, 2)} pounds.")

elif unit == "pounds":
    print(f"Your weight is {round(weight / 2.204623, 2)} Kilograms.")

else:
    print("You chose an invalid unit, please try again.")
