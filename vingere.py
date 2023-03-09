# shell project to crypt and decrypt a message using vingere cipher

# import modules
import sys

# define functions
def encrypt(message, key):
    #encrypt message using vingere cipher 
    # using a table
    # create table
    table = []
    # create alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # create table
    for i in range(26):
        # create row
        row = []
        # add alphabet to row
        for j in range(26):
            # add letter to row
            row.append(alphabet[(i + j) % 26])
        # add row to table
        table.append(row)
    # create encrypted message
    encrypted_message = ''
    # get length of message
    length_of_message = len(message)
    # get length of key
    length_of_key = len(key)
    # loop through message
    for i in range(length_of_message):
        # get letter
        letter = message[i]
        # get key letter
        key_letter = key[i % length_of_key]
        # get row
        row = alphabet.index(key_letter)
        # get column
        column = alphabet.index(letter)
        # get encrypted letter
        encrypted_letter = table[row][column]
        # add encrypted letter to encrypted message
        encrypted_message += encrypted_letter
    # return encrypted message
    return encrypted_message

def decrypt(message, key):
    #decrypt message using vingere cipher 
    # using a table
    # create table
    table = []
    # create alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # create table
    for i in range(26):
        # create row
        row = []
        # add alphabet to row
        for j in range(26):
            # add letter to row
            row.append(alphabet[(i + j) % 26])
        # add row to table
        table.append(row)
    # create decrypted message
    decrypted_message = ''
    # get length of message
    length_of_message = len(message)
    # get length of key
    length_of_key = len(key)
    # loop through message
    for i in range(length_of_message):
        # get letter
        letter = message[i]
        # get key letter
        key_letter = key[i % length_of_key]
        # get row
        row = alphabet.index(key_letter)
        # get column
        column = table[row].index(letter)
        # get decrypted letter
        decrypted_letter = alphabet[column]
        # add decrypted letter to decrypted message
        decrypted_message += decrypted_letter
    # return decrypted message
    return decrypted_message



def main():
    # main function
    # get command line arguments
    arguments = sys.argv
    # get number of arguments
    number_of_arguments = len(arguments)
    # check if number of arguments is correct
    if number_of_arguments != 4:
        # print usage
        print('Usage: python vingere.py [e|d] [message] [key]')
        # exit
        sys.exit(1)
    # get mode
    mode = arguments[1]
    # get message
    message = arguments[2]
    # get key
    key = arguments[3]
    # check if mode is encrypt
    if mode == 'e':
        # encrypt message
        encrypted_message = encrypt(message, key)
        # print encrypted message
        print(encrypted_message)
    # check if mode is decrypt
    elif mode == 'd':
        # decrypt message
        decrypted_message = decrypt(message, key)
        # print decrypted message
        print(decrypted_message)
    # mode is not valid
    else:
        # print usage
        print('Usage: python vingere.py [e|d] [message] [key]')
        # exit
        sys.exit(1)

# call main function
if __name__ == '__main__':
    main()
