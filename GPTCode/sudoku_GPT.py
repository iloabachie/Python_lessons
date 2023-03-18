# Here's a basic implementation of code to check if a solution to a 9x9 sudoku puzzle is valid:


def is_valid_sudoku(grid):
    # check each column
    for i in range(9):
        column = [grid[j][i] for j in range(9)]
        if not is_1_to_9(column):
            return False

    # check each row
    for row in grid:
        if not is_1_to_9(row):
            return False

    # check each of the 9 sub-grids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_1_to_9(subgrid):
                return False

    return True

def is_1_to_9(lst):
    return len(set(lst)) == 9 and all(map(lambda x: x in range(1, 10), lst))
# The is_valid_sudoku function takes a 2D list (a 9x9 grid) as input and returns True if the solution is valid, and False otherwise. The is_1_to_9 function takes a list of 9 integers as input and returns True if the list contains all the integers from 1 to 9 exactly once, and False otherwise.


# write python code to solve a 9x9 sudoku
# Here's an implementation of the backtracking algorithm to solve a 9x9 sudoku puzzle:


def solve_sudoku(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(grid, i, j, num):
                        grid[i][j] = num
                        if solve_sudoku(grid):
                            return True
                        grid[i][j] = 0
                return False
    return True

def is_valid(grid, row, col, num):
    # check row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # check column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # check sub-grid
    row_start = row - row % 3
    col_start = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + row_start][j + col_start] == num:
                return False
    return True
# The solve_sudoku function takes a 9x9 grid as input, where the empty cells are represented by the value 0. It uses a backtracking algorithm to find the solution. If a solution is found, it returns True, and the filled grid is stored in the input list. If no solution is found, it returns False.

# The is_valid function takes a 9x9 grid, a row and column number, and a number as input, and returns True if it's valid to place the number at the given cell in the grid, and False otherwise. It checks if the number is already present in the same row, column, or sub-grid.

