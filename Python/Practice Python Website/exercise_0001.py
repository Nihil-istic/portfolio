'''
Exercise 1

Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''

import datetime

year = datetime.datetime.now().year

while True:
        name = input('What is your name? ').strip()
        try:
            age = input(f'Hi {name}, how old are you? ').strip()
            age = int(age)
        except ValueError:
            print('You should type a numeric value for your age, try again\n')
            continue

        print(f'{name}, you will turn 100 years old by the year {100-age + year}!\n')