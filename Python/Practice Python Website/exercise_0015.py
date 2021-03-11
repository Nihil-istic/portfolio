'''
Exercise 15

Write a program (using functions!) that asks 
the user for a long string containing multiple 
words. 
Print back to the user the same string, except 
with the words in backwards order. 
For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me.
'''

def reverse_words(string):
    words = string.split()
    return ' '.join(a for a in words[::-1])

def main():
    while True:
        string = input('Enter a string: ').strip()
        print(reverse_words(string))
        print()

if __name__ == '__main__':
    main()
