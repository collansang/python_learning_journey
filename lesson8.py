#temperature converter from celsiuu\s to pounds and visw versa
temp = float(input("Please enter your temperature here: "))
unit = input("Is your temperature in celsius or fahrenheit(C, F)")

if unit == "C":
    temp = round(((9 * temp) / 5) + 32, 2)
    print(f"Your temperature is {temp} fahrenheit.")

elif unit == "F":
    temp = round((5/9) * (temp - 32), 2)
    print(f" Your temperature is {temp} celsius")

else:
    print("The input you entered is not recognized. please try again.")