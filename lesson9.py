#logical operators
#and: checks if both statements are true and returns True
#or: if one of he statements is true it returns True
#not : reverses the results


age = float(input("How old are you?: "))
weight = float(input("What is your weight in KGs?: "))
HIV_status = input("Are you HIV positive/negative(p/n)")

if age >= 18 and weight >=50 and HIV_status == "n":
    print("You meet all the qualifications to donate blood, "
          "Please donate at the nearest health facility to help a soul")

elif age >= 18 and weight <50 and HIV_status == "n":
    print("Your weight is too low, you dont qualify for a blood donation. Welcome back next time.")

elif 18> age >= 0 and weight >= 50 and HIV_status == "n":
    print("You should be 18+ years too donate your blood.")

elif age >= 18 and weight >= 50 and HIV_status =="p":
    print("You do not qualify for blood donations due to health issues, "
          "please conduct a certified medical practitioner for more assistance ")

elif age < 18 and weight < 50 or HIV_status == "p":
    print("You dont qualify for blood donations")



else:
    print("Please check your answers and enter them correctly")
