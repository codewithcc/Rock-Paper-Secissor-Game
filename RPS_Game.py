# ROCK PAPER SCISSORS GAME
# DEVLOPER : CHANCHAL ROY

from random import choice
values = ['ROCK','PAPER','SCISSORS']

def test(my_hand):
    com_hand = choice(values)
    if (my_hand == 'R' or my_hand == 'r') and com_hand == 'PAPER':
        return 'COM',com_hand

    elif (my_hand == 'R' or my_hand == 'r') and com_hand == 'SCISSORS':
        return 'ME',com_hand

    elif (my_hand == 'R' or my_hand == 'r') and com_hand == 'ROCK':
        return 'DRAW',com_hand

    elif (my_hand == 'P' or my_hand == 'p') and com_hand == 'ROCK':
        return 'ME',com_hand

    elif (my_hand == 'P' or my_hand == 'p') and com_hand == 'SCISSORS':
        return 'COM',com_hand

    elif (my_hand == 'P' or my_hand == 'p') and com_hand == 'PAPER':
        return 'DRAW',com_hand

    if (my_hand == 'S' or my_hand == 's') and com_hand == 'ROCK':
        return 'COM',com_hand

    elif (my_hand == 'S' or my_hand == 's') and com_hand == 'PAPER':
        return 'ME',com_hand

    elif (my_hand == 'S' or my_hand == 's') and com_hand == 'SCISSORS':
        return 'DRAW',com_hand

    else:
        print(f"Wrong Input Provided! {my_hand}\n")
        return 'None'

while True:
    my_hand = input('R for ROCK/P for PAPER/S for SCISSORS: ')
    data = test(my_hand)
    if data[0] == 'ME': print(f'You are the Winner! Computer says {data[1]}.\n')
    elif data[0] == 'COM' : print(f"Computer is the Winner! It says {data[1]}.\n")
    elif data[0] == 'DRAW' : print(f"The Game is Draw. Both says {data[1]}.\n")
    else: pass
