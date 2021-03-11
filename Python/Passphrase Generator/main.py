from secrets import choice
from argparse import ArgumentParser


def generate(word_list, word_count, separator, capitalize, numbers):
    if word_count < 4:
        return 'Your passphrase should be at least 4 words, but you should think about using at least 6.'
    
    elif len(separator) != 1:
        return 'Your separator should be only one character.'

    else:
        passphrase_list = [choice(word_list) for _ in range(word_count)]

        if capitalize:
            passphrase_list = [word.capitalize() for word in passphrase_list]

        if numbers:
            number_place = choice(list(range(len(passphrase_list))))
            passphrase_list[number_place] = passphrase_list[number_place] + choice([str(n) for n in range(10)])

        passphrase = separator.join(passphrase_list)
        return passphrase


def get_word_list(path):
    with open(path, 'r') as wl:
        return [word[:-1] for word in wl.readlines()]


if __name__ == '__main__':
    FILE = 'en.txt'

    parser = ArgumentParser(description='Create passphrases.')
    parser.add_argument('word_count', help='Number of words to use on your passphrase (At least 4).', type=int)
    parser.add_argument('separator', help='Character to put between each word.', type=str)
    parser.add_argument('-c', '--capitalize', help='Make uppercase each word\'s first letter.', action='store_true')
    parser.add_argument('-n', '--numbers', help='Add a number from 0 to 9 at the end of a random word.', action='store_true')

    args = parser.parse_args()

    print(
        generate(get_word_list(FILE), args.word_count, args.separator, args.capitalize, args.numbers)
    )
