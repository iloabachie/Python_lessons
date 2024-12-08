from typing import List, Tuple
from copy import deepcopy
from itertools import batched, chain

class Solution:        
    def display(self, board: List[List[str]]) -> None:
        print(f"Solution" if 0 not in chain(*board) else "Input")            
        for i in range(9):
            for _ in range(9):
                print(("+---" if _ % 3 else "‼---") if i % 3 else ("+===" if _ % 3 else "‼==="), end='')
            print("‼")
            for j in range(9):
                n = board[i][j]
                print(f"| {n if n else ' '} " if j % 3 else f"‼ {n if n else ' '} ", end='')
            print('‼')
        for _ in range(9):
            print("+===" if _ % 3 else "‼===", end='')
        print("‼")
        print()

    def display1(self, board):
        print("Solution" if 0 not in chain(*board) else "Input")   
        for i, row in enumerate(board):
            if i % 3 == 0 and i != 0:
                print("-" * 21)  # Print a horizontal separator every 3 rows
            for j, num in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")  # Print a vertical separator every 3 columns
                if num == 0:
                    print(". ", end="")  # Print a dot for empty cells
                else:
                    print(f"{num} ", end="")
            print()  # Move to the next line after each row
        print()

    def is_valid(self, coor: Tuple[int], guess: int, board: List[List[str]]) -> bool: 
        r, c = coor
        if guess in board[r]:
            return False
        for row in board:
            if guess == row[c]:
                return False        
        row_start = (r // 3) * 3
        col_start = (c // 3) * 3
        for a in range(row_start, row_start + 3):
            for b in range(col_start, col_start + 3):
                if guess == board[a][b]:
                    return False
        return True
    
    def next_free(self, board) -> Tuple[int]:
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    return r, c
        return None, None   
    
    def solveSudoku1(self, board: List[List[str]]) -> None:
        r, c = coor = self.next_free(board)
        if r is None:
            return True
        for guess in range(1, 10):
            if self.is_valid(coor, guess, board):
                board[r][c] = guess
                if self.solveSudoku1(board):
                    return True
            board[r][c] = 0 
    
    def solveSudoku2(self, board: List[List[str]]) -> None:
        r, c = coor = self.next_free(board)
        if r is None:
            return True
        for guess in reversed(range(1, 10)):
            if self.is_valid(coor, guess, board):
                board[r][c] = guess
                if self.solveSudoku2(board):
                    return True
            board[r][c] = 0  

def str_to_board(board_string: str) -> List[List[int]]:
    board = [[int(n) for n in row] for row in batched(board_string, 9)]
    return board


board = [
    [0, 0, 0, 0, 8, 0, 2, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 5, 0],
    [3, 0, 0, 0, 6, 0, 0, 0, 0],
    [0, 0, 7, 2, 0, 0, 0, 3, 0],
    [0, 8, 0, 9, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [6, 0, 0, 5, 0, 0, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

result = Solution()
result.display(board)

first = deepcopy(board)
result.solveSudoku1(first)
result.display1(first)

second = deepcopy(board)
result.solveSudoku2(second)
result.display(second)

# Hard
board = str_to_board('000800050097000000060000000200000040000370000000090600000500903800004000000000700')
result.display(board)
result.solveSudoku1(board)
result.display(board)

board = str_to_board('000800050097000000060000000200000040000370000000090600000500903800004000000000700')
result.display1(board)
result.solveSudoku2(board)
result.display(board)


board = str_to_board('603000070050090000000000000200705000080000904000300000000600800007000050400000000')
result.display1(board)
result.solveSudoku1(board)
result.display(board)