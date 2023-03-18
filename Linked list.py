class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def rotate(self, k):
        if not self.head or not self.head.next:
            return

        if k == 0:
            return

        if k > 0:
            for _ in range(k):
                self.tail.next = self.head
                self.head.prev = self.tail
                self.head = self.head.next
                self.head.prev = None
                self.tail = self.tail.next
                self.tail.next = None
        else:
            k = abs(k)
            for _ in range(k):
                self.head.prev = self.tail
                self.tail.next = self.head
                self.tail = self.tail.prev
                self.tail.next = None
                self.head = self.head.prev
                self.head.prev = None



def display_board():
    from os import system
    from time import sleep
    board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
    board = [ ['-' for i in range(3)] for j in range(3) ]
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
  

# display_board()



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

