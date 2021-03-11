'''
Exercise 12

Write a program that takes a list of numbers 
(for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last 
elements of the given list. For practice, write this 
code inside a function.
'''

def first_and_last(list):
    if len(list) > 0:
        return [list[0], list[-1]]

b = first_and_last(a:=[5, 10, 15, 20, 25])