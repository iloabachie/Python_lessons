'''youtuber = input("greeting ")
adj = "sesan"
print(youtuber)
matlib = f"computer{youtuber} and {adj} "
print(matlib)
'''
import random
'''
def guess(x):
    random_number = random.randint(2,x)
    guess = 0
    while guess!= random_number:
        guess = int(input(f"guess a numer bettween 1 and {x}: "))
        print(guess)'''

'''import random'''


'''def computer_guess(x, y):
    low = x
    high = y
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high, H, too low, L or correct, C: '))
        if feedback == "h":
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'yay! the ocmputer guessed your number , {guess} correctly')


computer_guess(1, 5000)'''


'''def play():
    user = input('r for rock, p for paper, or s for scissors: ')
    computer = random.choice(['r', 'p', 's'])
    if user == computer
    return 'tie'
    if user == 'p' and computer == 'r' or user == 'r' and computer == 's' or user == 's' and computer == 'p'
    return 'you win'
    return 'you lost'


print(play())'''


def play():
    user = input(
        "What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'


def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


play()
