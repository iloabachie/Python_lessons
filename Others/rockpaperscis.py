import random

scissors = '''
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
'''
paper = '''                           
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'       
'''
rock = '''
                      _    ,-,    _
                 ,--, /: :\/': :`\/: :\
                |`;  ' `,'   `.;    `: |
                |    |     |  '  |     |.
                | :  |     |     |     ||
                | :. |  :  |  :  |  :  | \
                 \__/: :.. : :.. | :.. |  )
                      `---',\___/,\___/ /'
                           `==._ .. . /'
                                `-::-'
'''

user = input("choose rock, paper or scissors r p or s:")
computer = random.choice(['r', 's', 'p'])
graphic = [rock, paper, scissors]


def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    # if player == 'r' or opponent == 'r':
    #     player = rock
    #     opponent = rock
    if player == opponent:
        return 'it is a tie'
    elif (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return 'you win'

    # return False
    return 'you lose'


print(f'user chose {user} computer chose {computer} therefore ')

print(is_win(user, computer))


# print(if 2 > 5 and 3 < 8)
