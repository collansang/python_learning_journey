#return function = statement used to end a function and send a result ack to the caller.
def add(x, y):
     z = x + y
     return z

def subtract(x, y):
     z = x - y
     return z

def multiply(x, y):
     z = x * y
     return z

def divide(x, y):
     z = x / y
     return z

print(add(3, 4))
print(subtract(3, 4))
print(multiply(3, 4))
print(divide(3, 4))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + ' ' + last

full_name = create_name('collan', 'kimtai')
print(full_name)