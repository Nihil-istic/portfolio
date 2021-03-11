'''
Exercise 4

Create a program that asks the user for a number 
and then prints out a list of all the divisors of that number. 

(If you don’t know what a divisor is, it is a number that 
divides evenly into another number. For example, 13 is a 
divisor of 26 because 26 / 13 has no remainder.)
'''

import pprint

while True:
    try:
        number = int(input('Enter a number: '))
    except ValueError:
        print('You have to type an integer number, try again\n')
        continue

    divisors = []

    for n in range(1, number + 1):
        if number % n == 0:
            divisors.append(n)
    
    print(f'The divisors of {number} are:')
    pprint.pprint(divisors)
    print()
    