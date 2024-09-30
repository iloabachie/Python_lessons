from typing import List, Tuple
from copy import deepcopy

class Solution:
    def display(self, board: List[List[str]]) -> None:
        for i in range(9):
            for _ in range(9):
                print("+---", end='')
            print("+")
            for j in range(9):
                print(f"| {board[i][j]} ", end='')
            print('|')
        for _ in range(9):
            print("+---", end='')
        print("+")
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


board = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 0, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
    ]


result = Solution()
result.display(board)

first = deepcopy(board)
result.solveSudoku1(first)
result.display(first)

second = deepcopy(board)
result.solveSudoku2(second)
result.display(second)
