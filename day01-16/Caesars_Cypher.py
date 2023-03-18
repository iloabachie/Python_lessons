# Day 8 final project

print('Welome to the Caesar\'s Cypher')


def encrypt():
    text = input('Type in message to be encrypted:\n> ').lower()
    shift = int(input('Enter encryption code:\n> '))
    alphabet = 'abcdefghijklmnopqrstuvwxyz!?,. '
    encrypted_word = ''
    for letter in text:
        if letter not in alphabet:
            encrypted_word += letter
        else:
            original_text_index = alphabet.index(letter)
            new_index = original_text_index + shift
            while new_index > len(alphabet) - 1:
                new_index = new_index - len(alphabet)
            encrypted_letter = alphabet[new_index]
            encrypted_word += encrypted_letter
    print(f'The encrypted message is:\n>{encrypted_word}')


def decrypt():
    text = input('Type in message to be decrypted:\n> ').lower()
    shift = int(input('Enter encryption code:\n> '))
    alphabet = 'abcdefghijklmnopqrstuvwxyz!?,. '
    decrypted_word = ''
    for letter in text:
        if letter not in alphabet:
            decrypted_word += letter
        else:
            original_text_index = alphabet.index(letter)
            new_index = original_text_index - shift
            while new_index < 0:
                new_index = new_index + len(alphabet)
            decrypted_letter = alphabet[new_index]
            decrypted_word += decrypted_letter
    print(f'The decrypted message is:\n>{decrypted_word}')


proceed = True
while proceed:
    action = input('E for encrypt or D for decrypt\n> ').lower()
    if action == 'e':
        encrypt()
        end = input(
            'Type yes to continue encoding or decoding otherwise type no\n> ').lower()
        while proceed:
            if end == 'yes':
                break
            elif end == 'no':
                proceed = False
            else:
                end = input(
                    'I do not understand the command, enter yes to continue or no to quit:\n>')
    elif action == 'd':
        decrypt()
        end = input('Type yes to encode/decode otherwise type no\n> ').lower()
        while proceed:
            if end == 'yes':
                break
            elif end == 'no':
                proceed = False
            else:
                end = input(
                    'I do not understand the command, enter yes to continue or no to quit:\n> ')
    else:
        print('Input error, please enter E for encrypt or D for decrypt!!!')
print('Thank you for using Caesar\'s Cypher')
