'''
Exercise 9

Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether 
they guessed too low, too high, or exactly right. 
'''

from random import randint

while True:
    number = randint(1,9)

    while True:
        try:
            guess = int(input('Guess the number: '))
            
        except ValueError:
            print('You should type an integer number')
            continue

        if guess > number:
            print(f'The number is smaller than {guess}')
        elif guess < number:
            print(f'The number is greater than {guess}')

        else:
            print('You did it!\n')
            break
