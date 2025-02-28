#rock , paper , scissors
import random
from enum import nonmember

options = ('rock', 'paper', 'scissors')
running =True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input('Enter a choice (Rock, paper, scissors)')
    print(f'player {player}')
    print(f'computer {computer}')

    if player == computer:
        print('Its a tie')
    elif player == 'rock' and computer == 'scissors':
        print('You win')
    elif player == 'scissors' and computer == 'papers':
        print('You win')
    elif player == 'paper' and computer == 'rock':
        print('You win')
    else:
        print('You loose')

    play_again = input('Play again? y/n').lower()
    if not play_again == 'y':
        running = False
print('Thanks for playing')