
def display_board():
    from os import system
    from time import sleep
    board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
    # board = [ ['-' for i in range(3)] for j in range(3) ]
    system('cls')
    print("+-------" * 3,"+", sep=""), sleep(0.2)
    for row in range(3):
        print("|       " * 3,"|", sep=""), sleep(0.2)
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end=""), sleep(0.2)
        print("|"), sleep(0.2)
        print("|       " * 3,"|",sep=""), sleep(0.2)
        print("+-------" * 3,"+",sep="")
    print([3 * 0 + i + 1 for i in range(3)])
    print([3 * 1 + i + 1 for i in range(3)])
    print([3 * 2 + i + 1 for i in range(3)])
    print(board)
  
display_board()


def totalFruit(fruits) -> int:
    basket, start, end = {}, 0, len(fruits)
    for fruit in fruits:
        basket[fruit] = basket.get(fruit, 0) + 1
        print(f'{basket=}')
        if len(basket) > 2:
            print(f'{start=},    {basket[fruits[start]]=}')
            basket[fruits[start]] -= 1
            if basket[fruits[start]] == 0:
                print(f'to be deleted {basket[fruits[start]]=}')
                del basket[fruits[start]]
            start += 1
    return end - start

fruits = [1,2,3,2,2, 3,3,3,3,3,2,1,2,3,3,3,2,2,2,1,1,1,1,1]

print(totalFruit(fruits))

import ConsolePrint

ConsolePrint.terminal_test()
ConsolePrint.ansi_codes()
