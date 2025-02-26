#consession stand programme
menu = {'rice_mix':60.00,
        'Chapati_beans':70.00,
        'Chips_kuku':450.00,
        'Kebub':40.00,
        'Soda':50,
        'Minutemaid':90.00}
cart = []
total = 0

print('----------- MENU -----------')
for key, value in menu.items():
    print(f'{key:20}: Ksh{value:.2f}')
print('-------------------------------')

while True:
    food = input('Please select the food you would like to have(q to quit)').lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

print('-------YOUR CART----------')
for food in cart:
    total += menu.get(food)
    print(food, end=' ')
print()
print('-------YOUR TOTAL----------')

print(f'Total is Ksh{total}')


