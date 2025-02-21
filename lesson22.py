#2d list
groceries = [['orange', 'pineapple', 'mango', 'tomato'],
             ['irish pitato', 'sweet potato', 'cassava'],
             ['chicken', 'beef', 'dove', 'rabbit']]
print(groceries[2][1]) #will print the element in the third row column 2 which is beef

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
