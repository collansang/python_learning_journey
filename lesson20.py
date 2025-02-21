#collections =  single variable used to store multiple values
        #list = []  ordered and changable, duplicates ok
        #set = {} unordered and immutable, but add and remove ok, no duplicatess
        #tuple = () ordered and unchangable , duplicates ok and is faster

fruits = ["mango", "orange", "peper", "pineapple", "apple"]
print(fruits[0]) # will print the first in the list

for fruit in fruits:
   print(fruit) #will print each in diffrent lines.
print(help(fruits)) #will print all descriptions of attributes available to youre codeie
print(len(fruits)) #will count the length of my string, in this case 5
print("pineapple" in fruits)# cheks if apple is present in our list, if present it returns True(boolean)
                              # and False if not

fruits[0] = "tomato" #will replace the first one with tomato
for fruit in fruits:
    print(fruit)

fruits.append("tomato")# Adds an element at the end of my list
print(fruits)

fruits.remove("apple")#will remove an element in the list
print(fruits)

fruits = {"mango", "orange", "peper", "pineapple", "apple"}
fruits.add("tomato") # adds tomato to my string
fruits.remove("apple") # removes apple
fruits.clear() #clears elements of a set
print(fruits)
