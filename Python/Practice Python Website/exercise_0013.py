'''
Exercise 13

Write a program that asks the user how many Fibonnaci 
numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the 
sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where 
the next number in the sequence is the sum of the previous two 
numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

while True:
    try:
        number = abs(int(input('How many numbers? ')))
    except ValueError:
        print('You should enter an integer number, try again\n')
        continue
    
    if number == 0:
        print()
    elif number == 1:
        print('0\n')
    else:
        fibonnaci = [0, 1]
        while len(fibonnaci) < number:
            fibonnaci.append(fibonnaci[-2] + fibonnaci[-1])
        print(f'{fibonnaci}\n')