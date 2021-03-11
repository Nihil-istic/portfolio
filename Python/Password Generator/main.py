from secrets import choice
from argparse import ArgumentParser

from string import ascii_lowercase as LOWER, ascii_uppercase as UPPER, digits as NUMBERS, punctuation as SPECIAL

parser = ArgumentParser(description='Python password generator by SalvadorBG')

parser.add_argument(
    'password_length',
    help='length for each generated password',
)

parser.add_argument(
    'number_of_passwords',
    help='number of passwords to generate',
)

parser.add_argument(
    '-l',
    '--no-lowercase',
    help='do not include lowercase characters',
    action='store_true'
)

parser.add_argument(
    '-u',
    '--no-uppercase',
    help='do not include uppercase characters',
    action='store_true'
)

parser.add_argument(
    '-n',
    '--no-numbers',
    help='do not include numeric characters',
    action='store_true'
)

parser.add_argument(
    '-s',
    '--no-special',
    help='do not include special characters',
    action='store_true'
)

arguments = parser.parse_args()

if arguments.no_lowercase and arguments.no_uppercase and arguments.no_numbers and arguments.no_special:
    print('No characters left')
    raise SystemExit

try:
    PASSWORD_LENGTH = int(arguments.password_length)
    NUMBER_OF_PASSWORDS = int(arguments.number_of_passwords)
except ValueError:
    print('[password_length] and [number_of_passwords] must be only numeric values')
    raise SystemExit

if PASSWORD_LENGTH < 4:
    print('[password_length] must be at least 4')
    raise SystemExit

if NUMBER_OF_PASSWORDS < 1:
    print('[number_of_passwords] must be at least 1')
    raise SystemExit

CHARSET = ''

if not arguments.no_lowercase:
    CHARSET += LOWER

if not arguments.no_uppercase:
    CHARSET += UPPER

if not arguments.no_numbers:
    CHARSET += NUMBERS

if not arguments.no_special:
    CHARSET += SPECIAL

for _ in range(NUMBER_OF_PASSWORDS):
    while True:
        password = ''

        for _ in range(PASSWORD_LENGTH):
            password += choice(CHARSET)

        if not arguments.no_lowercase:
            if not any(a in password for a in LOWER):
                continue

        if not arguments.no_uppercase:
            if not any(a in password for a in UPPER):
                continue

        if not arguments.no_numbers:
            if not any(a in password for a in NUMBERS):
                continue

        if not arguments.no_special:
            if not any(a in password for a in SPECIAL):
                continue

        break

    print(password)
