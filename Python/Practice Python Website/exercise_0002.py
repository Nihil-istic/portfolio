'''
Exercise 2

Ask the user for a number. 
Depending on whether the number is even or odd, 
print out an appropriate message to the user. 
'''

while True:
    try:
        number = int(input('Type a number: '))
    except ValueError:
        print('You should only type an integer number, try again\n')
        continue

    if number % 2 == 0:
        print('You have typed an even number\n')
    else:
        print('You have typed an odd number\n')

