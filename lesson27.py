#random number guessing game (mini-project)
import random
from queue import PriorityQueue

lowest_num = 1 #minimum number within our guess
highest_num = 100 #max number
answer = random.randint(lowest_num, highest_num) #answer collected randomly
guesses = 0 #will keep track of number of guesses we try
is_running = True

print('Python number guessing game')
print(f'Select the number between {lowest_num} and {highest_num}: ')

while is_running:
    gues= input('Enter your guess: ')
    if gues.isdigit():
        gues = int(gues)
        guesses += 1
        if gues < lowest_num or gues > highest_num:
            print('Your number is out of ange')
            print(f'Select the number between {lowest_num} and {highest_num}: ')
        elif gues < answer:
            print('Too small Try again')
        elif gues > answer:
            print('Too high Try again')

        else:
            print('Correct!!!!')
            print(f'Number of guesses:{guesses}' )

    else:
        print('Invalid guess ')
        print(f'Select the number between {lowest_num} and {highest_num}: ')

