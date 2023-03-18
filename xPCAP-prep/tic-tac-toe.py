import random
from os import system
from time import sleep
import sys
sys.path.append("D:\Documents\Python lessons\AngelaYu\Modulesx")
from countdown import loading1, loading2, loading3

system('cls')

'''
def boardDisplay():
    from os import system
    from time import sleep
    board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
    system('cls')
    print("+-------" * 3,"+", sep=""), sleep(1)
    for row in range(3):
        print("|       " * 3,"|", sep=""), sleep(1)
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end=""), sleep(1)
        print("|"), sleep(1)
        print("|       " * 3,"|",sep=""), sleep(1)
        print("+-------" * 3,"+",sep="")
    print([3 * 0 + i + 1 for i in range(3)])
    print([3 * 1 + i + 1 for i in range(3)])
    print([3 * 2 + i + 1 for i in range(3)])
    print(board)

boardDisplay()
'''

game_on = True
player_score = 0
computer_score = 0
game_number = 0

board_value = [ ['-' for i in range(3)] for j in range(3) ]

available_play = {
    '1': (0, 0),
    '2': (0, 1),
    '3': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '7': (2, 0),
    '8': (2, 1),
    '9': (2, 2)
}
        
def update_board(move, player):
    global board_value, available_play
    pos_tuple = available_play[move]    
    board_value[pos_tuple[0]][pos_tuple[1]] = 'O' if player == 'pc' else 'X'
    display_board()
    available_play.pop(move)

def display_board():
    board = f'''
    +-------+-------+-------+
    |       |       |       |
    |   {board_value[0][0]}   |   {board_value[0][1]}   |   {board_value[0][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board_value[1][0]}   |   {board_value[1][1]}   |   {board_value[1][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board_value[2][0]}   |   {board_value[2][1]}   |   {board_value[2][2]}   |
    |       |       |       |
    +-------+-------+-------+
    '''   
    print(board)

def enter_move():
    global available_play
    user_play = input('Your turn... ')
    while user_play not in available_play.keys() and game_on:
        user_play = input('Spot taken.  Choose your play: ')
    system('cls')
    print("You play...")
    update_board(user_play, 'human')

def score(): 
    gn = len(str(game_number))
    ps = len(str(player_score))
    cs = len(str(computer_score))
    spacep = '  '
    spacec = '  '
    if ps == 2:
        spacep = ' '
    if cs == 2:
        spacec = ' '
    
    print('+----------+----------+'), sleep(0.1)
    print(f'| Count    |        {game_number} |' if gn == 1 else f'| Count    |       {game_number} |')#, sleep(0.2)
    print('+----------+----------+'), sleep(0.1)
    print('| You      | Computer |'), sleep(0.1)
    print('+----------+----------+'), sleep(0.1)
    print(f'|      {spacep}{player_score} |      {spacec}{computer_score} |'), sleep(0.1)  
    print('+----------+----------+', end='\n\n'), sleep(0.1)
    
def victory():
    global game_on, player_score, computer_score, game_number
    computer = 'OOO'
    player = 'XXX'
    a = board_value[0][0]
    b = board_value[0][1]
    c = board_value[0][2]
    d = board_value[1][0]
    e = board_value[1][1]
    f = board_value[1][2]
    g = board_value[2][0]
    h = board_value[2][1]
    i = board_value[2][2]
    if computer in [a + b + c, d + e + f, g + h + i, a + d + g, b + e + h, c + f + i, a + e + i, c + e + g]:
        game_on = False
        game_number +=1
        computer_score += 1  
        print('Computer wins\n')
        score()
    
    elif player in [a + b + c, d + e + f, g + h + i, a + d + g, b + e + h, c + f + i, a + e + i, c + e + g]:         
        game_on = False
        game_number +=1
        player_score += 1
        print('You win\n')
        score()
        
    elif '-' not in a + b + c + d + e + f + g + h + i:
        game_on = False
        game_number +=1
        print('It is a draw\n')
        score()
        
    else:
        game_on = True

def smart_move():
    global available_play
        
    a = board_value[0][0]
    b = board_value[0][1]
    c = board_value[0][2]
    d = board_value[1][0]
    e = board_value[1][1]
    f = board_value[1][2]
    g = board_value[2][0]
    h = board_value[2][1]
    i = board_value[2][2]
    
    combi = [a + b + c, d + e + f, g + h + i, a + d + g, b + e + h, c + f + i, a + e + i, c + e + g]
    plays = ['XX-', 'OO-', 'X-X', 'O-O', '-XX', '-OO']
    print('|'.join(combi))
    if len(available_play) == 9:
        pc_move = random.choice(['1', '3', '5', '7', '9'])
    elif len(available_play) == 8:
        # y = random.choice(['1', '3', '5', '7', '9'])
        # pc_move = y if y in list(available_play.keys()) else random.choice(['1', '3', '5', '7', '9'].remove(y))
        pc_move = '5' if '5' in list(available_play.keys()) else random.choice(['1', '3', '7', '9'])
    elif "XX" not in '|'.join(combi) and 'OO' not in '|'.join(combi) and 'X-X' not in '|'.join(combi) and 'O-O' not in '|'.join(combi):
        pc_move = random.choice(list(available_play.keys()))
    elif plays[1] in '|'.join(combi) or plays[3] in '|'.join(combi) or plays[5] in '|'.join(combi):
        for _ in combi:
            condition = plays[1] == _ or plays[3] == _ or plays[5] == _
            if combi.index(_) == 0 and condition:
                options = ['1', '2', '3']
                for p in options:
                    if p in list(available_play.keys()):
                        pc_move = p
            elif combi.index(_) == 1 and condition:
                options = ['4', '5', '6']
                for p in options:
                    if p in list(available_play.keys()):
                        pc_move = p
            elif combi.index(_) == 2 and condition:
                options = ['7', '8', '9']
                for p in options:
                    if p in list(available_play.keys()):
                        pc_move = p
            elif combi.index(_) == 3 and condition:
                options = ['1', '4', '7']
                for p in options:
                    if p in list(available_play.keys()):
                        pc_move = p
            elif combi.index(_) == 4 and condition:
                options = ['2', '5', '8']
                for p in options:
                    if p in list(available_play.keys()):
                        pc_move = p
            elif combi.index(_) == 5 and condition:
                options = ['3', '6', '9']
                for p in options:
                    if p in list(available_play.keys()):
                        pc_move = p
            elif combi.index(_) == 6 and condition:
                options = ['1', '5', '9']
                for p in options:
                    if p in list(available_play.keys()):
                        pc_move = p
            elif combi.index(_) == 7 and condition:
                options = ['3', '5', '7']
                for p in options:
                    if p in list(available_play.keys()):
                        pc_move = p
    elif plays[0] in '|'.join(combi) or plays[2] in '|'.join(combi) or plays[4] in '|'.join(combi):        
        for _ in combi:
            condition = plays[0] == _ or plays[2] == _ or plays[4] == _
            if combi.index(_) == 0 and condition:
                options = ['1', '2', '3']
                for p in options:
                    if p in list(available_play.keys()):
                        pc_move = p
            elif combi.index(_) == 1 and condition:
                options = ['4', '5', '6']
                for p in options:
                    if p in list(available_play.keys()):
                        pc_move = p
            elif combi.index(_) == 2 and condition:
                options = ['7', '8', '9']
                for p in options:
                    if p in list(available_play.keys()):
                        pc_move = p
            elif combi.index(_) == 3 and condition:
                options = ['1', '4', '7']
                for p in options:
                    if p in list(available_play.keys()):
                        pc_move = p
            elif combi.index(_) == 4 and condition:
                options = ['2', '5', '8']
                for p in options:
                    if p in list(available_play.keys()):
                        pc_move = p               
            elif combi.index(_) == 5 and condition:
                options = ['3', '6', '9']
                for p in options:
                    if p in list(available_play.keys()):
                        pc_move = p
            elif combi.index(_) == 6 and condition:
                options = ['1', '5', '9']
                for p in options:
                    if p in list(available_play.keys()):
                        pc_move = p
            elif combi.index(_) == 7 and condition:
                options = ['3', '5', '7']
                for p in options:
                    if p in list(available_play.keys()):
                        pc_move = p
    else:
        pc_move = random.choice(list(available_play.keys()))
    
    system('cls')  
    print("Computer plays...")
    update_board(pc_move, 'pc')

def start_game():
    loading1(20) 
    sleep(0.5)
    system('cls')
    global board_value, game_on, available_play, play_again
    start = random.choice(['X', 'O'])
    print("Compouter starts..." if start == 'O' else "Player starts...")
    display_board()
    
    while game_on:
        if start == "O":
            loading2(2, 'thinking...')
            smart_move()
            victory()
            if game_on:
                enter_move()
                victory()
        else:
            enter_move()
            victory()
            if game_on:
                loading2(2, 'thinking...')
                smart_move()
                victory()
                
    play_again = input('Play again? Y or N?: ').lower()
    
    while play_again == 'y' or play_again == '':
        system('cls')
        game_on = True
        available_play = {
            '1': (0, 0),
            '2': (0, 1),
            '3': (0, 2),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '7': (2, 0),
            '8': (2, 1),
            '9': (2, 2)
        }
        board_value = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]
        start_game()
    
start_game()

print('\nThank you for playing\n')
