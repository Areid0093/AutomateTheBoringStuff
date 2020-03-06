import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')

import random

guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')

    guess = input()

# 0 is tails, 1 is heads

if (toss := random.randint(0, 1)) == 0:
    toss = 'tails'
else:
    toss = 'heads'
    
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    # guess = input()
    if toss == (guess := input()):
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')