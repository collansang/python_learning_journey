#function = A block of reusable code
#           You place () after the function to invoke it.

def happy_birthday(name, age):
    print(f'Happy birthday {name} *2')
    print(f'Happy birthday dear {name} ')
    print('Hapy birthday to you. ')
    print(f'How old are you now?. {age} ')
    print() # will skip a line before repeating.
happy_birthday('Collan', 20)
happy_birthday('Abel', 21)
happy_birthday('Moses', 23)


def display_invoice(username, amount, due_date):
    print(f'Hello {username}')
    print(f'Your bill of {amount}, is due {due_date}')
    print()
display_invoice('Moses', 20.00, '01 jan 2025')
display_invoice('Kibe', 100.00, '03 feb 2025')