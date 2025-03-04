#arbitrary arguments = allows you to pass multiple non-key arguments and keyword arguments
                        #1. positional, 2. default, 3. keyword 4, arbitrary
                        # *args = arguments
                        #*kwargs = keyword arguments


#*args
def add(*args): # will add as many numbers as you wish
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,2,3))



def names(*args):
    for arg in args:
        print(arg, end=' ')
names('Dr.', 'Collan', 'Kimtai', 'Sang')



#*kwags