#Typecasting = the process of converting a variable from one data type to another  ex str(). int(). float(). bool().

name = "collan"
age = 20
points = 75.48
is_student = True

points = int(points)
print (points)
age =float (age)
print (age)
age =str(age)
print(type(age))


#input() = a function that prompts the user to enter data and it returns the entered data as a string
Jina = input("unaitwa nani boss?:")
staff=input("Karibu sana. Leo unadai kubuy staff gani?:")
staff_price = float(input("Staff yako ni hw much?:"))
staff_no= int(input("Unadai kubuy ngapi?:"))
print(f"Holla {Jina} ")
messo =(f"Unadai kununua {staff} {staff_no}?")
print(f"Total cost ya staff yako ni {staff_price * staff_no}Ksh")
print(f"Shukran kutuchagua sisi na karibu tena {Jina} ")

