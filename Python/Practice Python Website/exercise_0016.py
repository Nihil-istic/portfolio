'''
Exercise 16

Write a password generator in Python. 
Be creative with how you generate passwords - strong 
passwords have a mix of lowercase letters, uppercase 
letters, numbers, and symbols. 
The passwords should be random, generating a new 
password every time the user asks for a new password. 
Include your run-time code in a main method.
'''

from secrets import choice
from string import digits, ascii_lowercase, ascii_uppercase, punctuation

LENGHT = 16
ALL = ascii_lowercase + ascii_uppercase + digits + punctuation

def generate(lenght, set):

    while True:
        password = ''.join(choice(set) for _ in range(lenght))

        if (
            any(a in digits for a in password) and 
            any(a in ascii_lowercase for a in password) and 
            any(a in ascii_uppercase for a in password) and 
            any(a in punctuation for a in password)
        ):
            return password
        
        else:
            continue

def main():
    while True:
        print(generate(LENGHT, ALL))
        input('\nPress enter to generate another password')

if __name__ == "__main__":
    main()