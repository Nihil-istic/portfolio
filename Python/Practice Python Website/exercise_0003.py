'''
Exercise 3

Take a list and write a program that 
prints out all the elements of the list 
that are less than 5.
'''

LIST = [i for i in range(-1_000, 1_001)]

for n in LIST:
    if n < 5: print(n)