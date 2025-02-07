#indexing  = allows us to access the ellements of a sequence using [] (indexing operator)
#[ start : end : end]


phone_number = "254746581478"
print(phone_number[0]) # prints the first digit in which is : 2 ,

#how to print first few digits of the string
#string_name [start : end : step]

code_number = "0987654321"
print(code_number[0:4]) # you can omit the 0 and start from the colon because python will
                        # automatically begin from the beginning of the string
print (code_number[:4]) #0 omited provides same results as above

# how to print last few digits in a string
#you start with starting point then a colon, then python will print from your starting point to the end

random_no = "9807594568"
print(random_no[5 : ]) #prints from the fifth digit to the last

#how to print a specific digits in the string
russia = "1254789767584732"
print(russia[2 : 4]) # will print the 2th and 3rd

#how to print the last digit of the string
# you just use -1 within the parenthesis
china = "6846278361279634982146"
print(china[-1]) # if you replace -1 with -2 it will print the 2nd last , if -3 it prints 3rd last and so fourth

collani = "549266547"
print(collani[::2])# counts every second digit in the string starting from the first digit ,
                    # ,if we replace 2 with 3 it will print the 3rd etc


#how to reverse a string
sang = "1234567890"
print(sang[::-1])# reverses the string

##exercise
#print the first 3 and last 4 digits of your phone number


phone_no = input("Please enter your phone number:" )
first_3 = (phone_no[: 3])
last_3 = (phone_no[-4: ])
print(f"Are you the owner of {first_3} xxx xx {last_3} ")






