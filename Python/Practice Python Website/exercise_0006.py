'''
Exercise 6

Ask the user for a string and print out whether this 
string is a palindrome or not. 
(A palindrome is a string that reads the same 
forwards and backwards.)
'''

while True:
    palindrome = input('Enter a string: ').strip().lower()

    reversed = ''.join(a for a in list(palindrome)[::-1])

    if palindrome == reversed:
        print(f'{palindrome} is a palindrome!\n')
    else:
        print(f'{palindrome} is not palindrome!\n')
