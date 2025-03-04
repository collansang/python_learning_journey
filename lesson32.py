#keyword arguments = an argument preceded by an identifier
                    #helps with readability
                    #1. positional, 2. default, 3. keyword 4, arbitrary

for x in range(1, 11):
    print(x, end=' ') # will end it in one line
print()
print('1','2', '3', '4', '5', sep='-') # will separate numbers with a hyphen



def get_phone(country, area, first, last):
    return f'{country}-{area}-{first}-{last}'
phone_number = get_phone(country= '+254',area=7 ,first=4658,last=1478)
print(phone_number)
