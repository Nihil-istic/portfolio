'''
Exercise 14

Write a program (function!) that takes a 
list and returns a new list that contains all 
the elements of the first list minus all the duplicates.
'''

def remove_duplicates(list):
    new_list = []
    [new_list.append(a) for a in list if a not in new_list]
    return new_list