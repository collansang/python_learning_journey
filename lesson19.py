#nested loops  = a loop within another loop
# outer loop:
     #inner loop:


# for x in range(2):#will create the loop two times
#     for x in range(1, 11):
#         print(x, end=",")
#     print()#will print the repeating loop in a diffrent line


rose = int(input("Enter th number of rows. "))
columns = int(input("Enter the number of columns. "))
symbol = input("Enter the symbol to use. ")
for x in range(rose):
    for x in range (columns):
        print(symbol, end=",")
    print()
