'''
Description
Easy implementation to hashing strings using sha512

It has three functions:
    generate(string, salt=None) to generate a sha512 string from plain text
    
    iterate(string, iterations, salt=None) to interate generate() over itself as many times as specified
    
    check_hash(hashed, plain_text, iterations) to validate a hashed string and its corresponding plain_text and salt
    
salt argument should be left empty (ignored)

Last update: August 03, 2020 
'''

from uuid import uuid4
from hashlib import sha512

def generate(string, salt=None):
    '''
    Parameters
    string: plain text string up to 2 to the power of 128 characters
    salt: if there is a defined salt to add, use it, if not, ignore

    Description
    fuction that takes a plain text string and returns its sha512 salted hash 
    in the format:
    [half of salted hash][half of salt][:][other half of salt][other half of salted hash] 
    '''

    if salt == None:
        salt = uuid4().hex

    hash_object = sha512( salt.encode('UTF-8') + string.encode('UTF-8') )
    hex_dig = hash_object.hexdigest()

    return hex_dig[:64] + salt[:16] + ':' + salt[16:] + hex_dig[64:]

def iterate(string, iterations, salt=None):
    '''
    Parameters
    string: plain text string up to 2 to the power of 128 characters
    iterations: number of times generate() will be used over itself
    salt: if there is a defined salt to add, use it, if not, ignore

    Description
    function that takes a plain text string and a number of iterations
    generates a hash over itself as many times as iterations value
    '''
    hash = string

    for _ in range(iterations):
        hashed = generate(hash, salt)
        hash, salt = hashed[:64] + hashed[-64:], hashed[64:80] + hashed[81:-64]

    return hash[:64] + salt[:16] + ':' + salt[16:] + hash[64:]


def check_hash(hashed, plain_text, iterations):
    '''
    Parameters
    hashed: the hash of the plain text you are going to validate
    plain_text: very descriptive, a plain text to compare with hashed
    iterations: number of iterations to apply to plain_text

    Description
    function that takes a hashed string (the stored one), a plain_text to validate and
    the number of iterations to apply to plain_text
    it compares the finished hashed plain_text to the hashed string and returns True if they are equal
    '''

    salt = hashed[64:80] + hashed[81:-64]
    
    new_hash = iterate(plain_text, iterations, salt)

    return hashed == new_hash

if __name__ == '__main__':
    print('Is everything working?')
    print( 
        check_hash(
            iterate('This is a test', 100_000), 
            'This is a test', 100_000
            ) 
        and 
        check_hash(
            generate('This is a test'), 
            'This is a test', 1
            ) 
        )
