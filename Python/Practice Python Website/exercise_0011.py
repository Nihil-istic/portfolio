'''
Exercise 11

Ask the user for a number and determine whether 
the number is prime or not. (For those who have forgotten, 
a prime number is a number that has no divisors). 
'''

while True:
    try:
        number = int(input('Enter a number: '))
    except ValueError:
        print('You should enter an integer number')

    for n in range(2, number):
        if number % n == 0:
            print(f'{number} is not prime\n')
            break
    else:
        print(f'{number} is prime\n')