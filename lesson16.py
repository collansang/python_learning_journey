#python compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Please enter your principle amount"))
    if principle < 0:
        print("Principle cannot be less than 0 ")
    else:
        break

while True:
    rate = float(input("Please enter your rate"))
    if rate < 0:
        print("Principle cannot be less than 0 ")
    else:
        break

while True:
    time = int(input("Please enter your time in years"))
    if time <= 0:
        print("time cannot be less than 0 ")
    else:
        break

total = principle * pow((1+rate/100), time)

print( f"Your balance after {time} years is {total:.2f}")