def guess_game():
    import random
    print('Welcome to the guessing game!!!')

    level = ''
    while level != 'e' or level != 'h':
        level = input('choose dificulty E for Easy H for hard').lower()
        if level == 'e':
            attempts = 10
            break
        elif level == 'h':
            attempts = 5
            break
        else:
            print('invalid entry, try again')

    digit = random.randint(1, 100)
    print('I am thinking of a number between 1 and 100')

    while attempts > 0:
        print(f'you have {attempts} attempts left\nMake a guess')
        guess = int(input('Guess the number: '))
        if guess > digit:
            print(f'Your guess {guess} is too high')
        elif guess < digit:
            print(f'Your guess {guess} is too low')
        else:
            print(f'you guess {guess} is correct')
            break
        attempts -= 1
    if guess == digit:
        pass
    else:
        print(f'You lost, you have {attempts} attempts left.')

    new_game = input('do you want to play again: ').lower()
    if new_game == 'y':
        guess_game()
    else:
        pass
    print('Thank you for playing')


guess_game()
