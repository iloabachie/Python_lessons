import random

def generate_code():
    """Generates a random 4-digit code."""
    code = ""
    for i in range(4):
        code += str(random.randint(0, 9))
    return code

def get_guess():
    """Asks the player for a 4-digit guess."""
    guess = input("Enter your 4-digit guess: ")
    while len(guess) != 4 or not guess.isdigit():
        guess = input("Invalid input. Enter your 4-digit guess: ")
    return guess

def get_hint(code, guess):
    """Returns a hint for the guess based on the code."""
    hint = ""
    for i in range(4):
        if guess[i] == code[i]:
            hint += "MATCH "
        elif guess[i] in code:
            hint += "CLOSE "
        else:
            hint += "NOPE "
    return hint

def play_game():
    """Plays the code breaker game."""
    code = generate_code()
    print("The code has been generated. Start guessing!")
    guesses = 0
    while True:
        guess = get_guess()
        guesses += 1
        hint = get_hint(code, guess)
        print(hint)
        if guess == code:
            print("Congratulations! You guessed the code in", guesses, "guesses.")
            break

play_game()
