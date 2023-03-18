

board1 = [
295743861,
431865927,
876192543,
387459216,
612387495,
549216738,
763524189,
928671354,
154938672
]

board2 = [
195743862,
431865927,
876192543,
387459216,
612387495,
549216738,
763524189,
928671354,
254938671
]

board3 = [
    [".",".","4",".",".",".","6","3","."],
    [".",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".","9","."],
    [".",".",".","5","6",".",".",".","."],
    ["4",".","3",".",".",".",".",".","1"],
    [".",".",".","7",".",".",".",".","."],
    [".",".",".","5",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
    ]

def board_var(board):
    if isinstance(board[0], list): board = [''.join(item) for item in board]
    if type(board[0]) == int: board = [str(item) for item in board]
    global b00, b01, b02, b03, b04, b05, b06, b07, b08, b10, b11, b12, b13, b14, b15, b16, b17, b18, b20, b21, b22, b23, b24, b25, b26, b27, b28, b30, b31, b32, b33, b34, b35, b36, b37, b38, b40, b41, b42, b43, b44, b45, b46, b47, b48, b50, b51, b52, b53, b54, b55, b56, b57, b58, b60, b61, b62, b63, b64, b65, b66, b67, b68, b70, b71, b72, b73, b74, b75, b76, b77, b78, b80, b81, b82, b83, b84, b85, b86, b87, b88
    b00 = board[0][0]
    b01 = board[0][1]
    b02 = board[0][2]
    b03 = board[0][3]
    b04 = board[0][4]
    b05 = board[0][5]
    b06 = board[0][6]
    b07 = board[0][7]
    b08 = board[0][8]

    b10 = board[1][0]
    b11 = board[1][1]
    b12 = board[1][2]
    b13 = board[1][3]
    b14 = board[1][4]
    b15 = board[1][5]
    b16 = board[1][6]
    b17 = board[1][7]
    b18 = board[1][8]

    b20 = board[2][0]
    b21 = board[2][1]
    b22 = board[2][2]
    b23 = board[2][3]
    b24 = board[2][4]
    b25 = board[2][5]
    b26 = board[2][6]
    b27 = board[2][7]
    b28 = board[2][8]

    b30 = board[3][0]
    b31 = board[3][1]
    b32 = board[3][2]
    b33 = board[3][3]
    b34 = board[3][4]
    b35 = board[3][5]
    b36 = board[3][6]
    b37 = board[3][7]
    b38 = board[3][8]

    b40 = board[4][0]
    b41 = board[4][1]
    b42 = board[4][2]
    b43 = board[4][3]
    b44 = board[4][4]
    b45 = board[4][5]
    b46 = board[4][6]
    b47 = board[4][7]
    b48 = board[4][8]

    b50 = board[5][0]
    b51 = board[5][1]
    b52 = board[5][2]
    b53 = board[5][3]
    b54 = board[5][4]
    b55 = board[5][5]
    b56 = board[5][6]
    b57 = board[5][7]
    b58 = board[5][8]

    b60 = board[6][0]
    b61 = board[6][1]
    b62 = board[6][2]
    b63 = board[6][3]
    b64 = board[6][4]
    b65 = board[6][5]
    b66 = board[6][6]
    b67 = board[6][7]
    b68 = board[6][8]

    b70 = board[7][0]
    b71 = board[7][1]
    b72 = board[7][2]
    b73 = board[7][3]
    b74 = board[7][4]
    b75 = board[7][5]
    b76 = board[7][6]
    b77 = board[7][7]
    b78 = board[7][8]

    b80 = board[8][0]
    b81 = board[8][1]
    b82 = board[8][2]
    b83 = board[8][3]
    b84 = board[8][4]
    b85 = board[8][5]
    b86 = board[8][6]
    b87 = board[8][7]
    b88 = board[8][8]        
    
    display = f'''
    +---+---+---+---+---+---+---+---+---+
    | {b00} | {b01} | {b02} | {b03} | {b04} | {b05} | {b06} | {b07} | {b08} |
    +---+---+---+---+---+---+---+---+---+    
    | {b10} | {b11} | {b12} | {b13} | {b14} | {b15} | {b16} | {b17} | {b18} |
    +---+---+---+---+---+---+---+---+---+ 
    | {b20} | {b21} | {b22} | {b23} | {b24} | {b25} | {b26} | {b27} | {b28} |
    +---+---+---+---+---+---+---+---+---+ 
    | {b30} | {b31} | {b32} | {b33} | {b34} | {b35} | {b36} | {b37} | {b38} |
    +---+---+---+---+---+---+---+---+---+ 
    | {b40} | {b41} | {b42} | {b43} | {b44} | {b45} | {b46} | {b47} | {b48} |
    +---+---+---+---+---+---+---+---+---+ 
    | {b50} | {b51} | {b52} | {b53} | {b54} | {b55} | {b56} | {b57} | {b58} |
    +---+---+---+---+---+---+---+---+---+ 
    | {b60} | {b61} | {b62} | {b63} | {b64} | {b65} | {b66} | {b67} | {b68} |
    +---+---+---+---+---+---+---+---+---+ 
    | {b70} | {b71} | {b72} | {b73} | {b74} | {b75} | {b76} | {b77} | {b78} |
    +---+---+---+---+---+---+---+---+---+ 
    | {b80} | {b81} | {b82} | {b83} | {b84} | {b85} | {b86} | {b87} | {b88} |
    +---+---+---+---+---+---+---+---+---+    
    '''
    print(display)

def board_display(board):
    board_var(board)
    display = f'''
    +---+---+---+---+---+---+---+---+---+
    | {b00} | {b01} | {b02} | {b03} | {b04} | {b05} | {b06} | {b07} | {b08} |
    +---+---+---+---+---+---+---+---+---+    
    | {b10} | {b11} | {b12} | {b13} | {b14} | {b15} | {b16} | {b17} | {b18} |
    +---+---+---+---+---+---+---+---+---+ 
    | {b20} | {b21} | {b22} | {b23} | {b24} | {b25} | {b26} | {b27} | {b28} |
    +---+---+---+---+---+---+---+---+---+ 
    | {b30} | {b31} | {b32} | {b33} | {b34} | {b35} | {b36} | {b37} | {b38} |
    +---+---+---+---+---+---+---+---+---+ 
    | {b40} | {b41} | {b42} | {b43} | {b44} | {b45} | {b46} | {b47} | {b48} |
    +---+---+---+---+---+---+---+---+---+ 
    | {b50} | {b51} | {b52} | {b53} | {b54} | {b55} | {b56} | {b57} | {b58} |
    +---+---+---+---+---+---+---+---+---+ 
    | {b60} | {b61} | {b62} | {b63} | {b64} | {b65} | {b66} | {b67} | {b68} |
    +---+---+---+---+---+---+---+---+---+ 
    | {b70} | {b71} | {b72} | {b73} | {b74} | {b75} | {b76} | {b77} | {b78} |
    +---+---+---+---+---+---+---+---+---+ 
    | {b80} | {b81} | {b82} | {b83} | {b84} | {b85} | {b86} | {b87} | {b88} |
    +---+---+---+---+---+---+---+---+---+    
    '''
    print(display)
    
    
def sudoku(board):
    from collections import Counter
    board_display(board)
    aim = Counter('123456789')
    horizontal = []
    vertical = []
    for item in board:
        horizontal.append(aim == Counter(str(item)))
    print(horizontal)
    
    for index in range(9):
        vertical_string = ''
        for item in board:
            item = str(item)
            vertical_string += item[index]
        vertical.append(aim == Counter(vertical_string))
    print(vertical)
    
    board_var(board)
    square1 = b00 + b01 + b02 + b10 + b11 + b12 + b20 + b21 + b22
    square2 = b03 + b04 + b05 + b13 + b14 + b15 + b23 + b24 + b25
    square3 = b06 + b07 + b08 + b16 + b17 + b18 + b26 + b27 + b28
    square4 = b30 + b31 + b32 + b40 + b41 + b42 + b50 + b51 + b52
    square5 = b33 + b34 + b35 + b43 + b44 + b45 + b53 + b54 + b55
    square6 = b36 + b37 + b38 + b46 + b47 + b48 + b56 + b57 + b58
    square7 = b60 + b61 + b62 + b70 + b71 + b72 + b80 + b81 + b82
    square8 = b63 + b64 + b65 + b73 + b74 + b75 + b83 + b84 + b85
    square9 = b66 + b67 + b68 + b76 + b77 + b78 + b86 + b87 + b88
    square_check = []
    squares = [square1, square2, square3, square4, square5, square6, square7, square8, square9]
    for item in squares:
        square_check.append(Counter(item) == aim)
    print(square_check)
    
    print("Congratulations, Board is Solved" if False not in square_check + vertical + horizontal else "Errors remain!!!")
    
    
from time import time
start1 = time()
sudoku(board1)
print('Board 1 time: ',time() - start1)

board_var(board3)