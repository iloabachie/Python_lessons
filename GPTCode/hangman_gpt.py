"""Hangman as produced by ChatGPT"""

import random, os, string, time

wordlist = ["python", "spark", "kubernetes", "go", "javascript", "basic", "fortran", "java", "linux", "bootstrap", "angular", "docker", "terraform"]
word = random.choice(wordlist)
word_mask = ["_"] * len(word)
incorrect_guesses = []
remaining_guesses = 6

def check_guess(guess):
    global word_mask
    global incorrect_guesses
    global remaining_guesses
    if guess == "cheat":
        remaining_guesses += 2
    elif len(guess) != 1 or guess not in string.ascii_lowercase:
        print("You entered an invalid input: ", guess)
        time.sleep(1)
    elif guess in word_mask:
        print(f"You already guessed \"{guess}\" correctly")
        time.sleep(1)
    elif guess in word:
        print("Correct: ", guess)
        time.sleep(1)
        for i in range(len(word)):
            if word[i] == guess:
                word_mask[i] = guess  
    elif guess in incorrect_guesses:
        print("You already guessed", guess)
        time.sleep(1)
    else:
        print("Wrong guess: ", guess)
        time.sleep(1)
        incorrect_guesses.append(guess)
        incorrect_guesses = sorted(incorrect_guesses)
        remaining_guesses -= 1
    
def print_game_state():
    os.system('cls')
    print("**H A N G M A N**\n")
    print("|", " ".join(word_mask), "|")
    print("Incorrect guesses: ", incorrect_guesses)
    print("Remaining guesses: ", remaining_guesses)
    time.sleep(0.5)

def main():
    while True:
        print_game_state()
        if "_" not in word_mask:
            print("You win!!!")
            break
        elif remaining_guesses == 0:
            print("You lose! Hidden word is: ", word.upper())
            break
        guess = input("Enter a letter: ").lower()
        check_guess(guess)

while True:
    main()
    time.sleep(1)
    proceed = input("Would you like to play again? y or n: ").lower()
    if proceed == 'n':
        print("Thank you for playing...")
        break
    else:
        word = random.choice(wordlist)
        word_mask = ["_"] * len(word)
        incorrect_guesses = []
        remaining_guesses = 6
        