import random

image = {
    'scissors': r'''
     _       ,/'
    (_).  ,/'
     __  ::
    (__)'  `\.
                `\.
    ''',
    'paper': r'''                           
            ___..__
    __..--""" ._ __.'
                "-..__
                '"--..__";
    ___        '--...__"";
        `-._   '"---..._;"
            *===----'       
    ''',
    'rock': r'''
           _    ,-,    _
    ,--, /: :\/': :`\/:  \
    |`;  ' `,'   `.;    `:\
    |    |     |  '  |     |.
    | :  |     |     |     ||
    | :. |  :  |  :  |  :  | 
     \__/: :.. : :.. | :.. |  )
          `---',\___/,\___/ /'
            `==._ .. . /'
                    `-::-'
    '''
}
    
print(image['rock'], image['paper'], image['scissors'])

user = input("choose rock, paper or scissors r p or s:")
user = 'rock' if user=='r' else 'paper' if user=='p' else 'scissors'
computer = random.choice(['rock', 'scissors', 'paper'])


def is_win(player, opponent):
    if player == opponent:
        return 'it is a tie'
    elif (player[0] == 'r' and opponent[0] == 's') or (player[0] == 's' and opponent[0] == 'p') or (player[0] == 'p' and opponent[0] == 'r'):
        return 'you win'
    return 'you lose'


print(f'You chose\n{image[user]}\ncomputer chose\n{image[computer]}\ntherefore\n\n{is_win(user, computer)}')
