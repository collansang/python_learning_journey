#format specifiers = {value:flags} formats a value based on what flags are inserted

# .(number)f = rounds off to that number in brackets
# :(number) = allocate the many spaces
# :03 = allocate and zero pad that man speces
# :< = left justify
# :> right justify
# :^ = center align
# :+ = uses a plus sign to indicate a positive value
# := = place sign to left most position
# : = insert a space before positive numbers
# :, = comma separater

price1 = 3.34554
price2 = 12.3489735
price3 = 3789.65312869

# print(f"Price 1 is Ksh{price1 : .2f}")  # converts  to 2dp
# print(f"Price 2 is Ksh{price2 : .2f}")  # converts  to 2dp
# print(f"Price 3 is Ksh{price3 : .2f}")   # converts  to 2dp

price4 = 1224.12424
price5 = 76.545
price6 = 7569.58905

# print(f"Price4 is Ksh {price4 : 10}") #value has 10 spaces to display the output.
# print(f"Price5 is Ksh {price5 : 10}") #value has 10 spaces to display the output.

# print(f"Price4 is Ksh {price4 : 010}") #value has 10 spaces to display the output. and is 0 paded
# print(f"Price5 is Ksh {price5 : 010}") #value has 10 spaces to display the output. and is 0 paded

# print(f"Price4 is Ksh {price4 : <10}") #value has 10 spaces to display the output. and is left justified
# print(f"Price5 is Ksh {price5 : <10}") #value has 10 spaces to display the output. and is left justified


# print(f"Price 1 is Ksh{price1 :+}")  # displayys a plus sign to positive values( altanatively just skip a space as belw)
# print(f"Price 2 is Ksh{price2 : }")  # displayys a plus sign to positive values
# print(f"Price 3 is Ksh{price3 :+}")   # displayys a plus sign to positive values


print(f"Price 1 is Ksh{price1 :,}") #separates digits in thousanths 3s
print(f"Price 2 is Ksh{price2 :,}")
print(f"Price 3 is Ksh{price3 :,}")