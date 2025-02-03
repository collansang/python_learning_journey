#usefull expressions

#name = input("Enter your full name: ")

#results = len(name)# counts the length of the string ,
#results = name.find(" ") #returns the position of a given
           #character. in this case blank space. counts starting from 0
#results = name.rfind("l")# will return the position of l from the other end (reverse)
#iff there are no results in finding it the result is -1
#results = name.capitalize() #capitalizes only the first letter of the string.
#results = name.upper()#capitalize all the string
#results = name.lower() #makes a string lower case
#results = name.isdigit() #returns true if the string is
          # only made of digits(numbers) otherwise it returns false
#results = name.isalpha() #returns true only if the string contains only alphabetical
           # charecters.nb it returns false als when blenk space is present
#print(results)

phone_no = input("Please input your phone number?: ")
#results = phone_no.count("-") #counts dashes from the string
#print(results)

phone_no= phone_no.replace("-"," ")# replaces a string t the n of your choice,,,
           # replaced my dash with a space on the phone number
print(phone_no)
