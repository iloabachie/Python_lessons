def add(c, k):
    c.test += 1
    k += 1

class Plus:
    def __init__(self):
        self.test = 0

def main():
    p = Plus()
    index = 0
    
    for i in range(0, 25):
        add(p, index)
        
    print(p.test, index)

main()

f = None
for i in range(5):
    with open("app.log", "w") as f:
        print(f.closed)
        if i > 2:
            break

print(f.closed)

data = [1,2,3,4,5,6]
import copy
try: 
    newList = copy.copy(data)
    print("1 passed")
    print(id(data), id(newList))
except: 
    print('1 failed')
try: 
    newList = data.copy()
    print("2 passed")
    print(id(data), id(newList))
except:
    print('2 failed')
try:
    newList.copy(data)
    print('3 passed')
    print(id(data), id(newList))
except:
    print('3 failed')
try:
    newList = list(data)
    print('4 passed')
    print(id(data), id(newList))
except:
    print('4 failed.')
    
    
class Solution:
    def __init__(self):
        self.count = 0

    def uniquePaths(self, m: int, n: int) -> int:
        row, col = m - 1, n - 1

        def trace(r, c):
            if r == row + 1 or c == col + 1:
                return
            if r == row and c == col:
                self.count += 1
                return
            
            trace(r, c + 1)
            trace(r + 1, c)
                      
        trace(0, 0)
        return self.count


print(Solution().uniquePaths(10,10))





print("-----------------------")

import random
class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        print(dungeon)
        row, col = len(dungeon), len(dungeon[0])
        totals = []

        def trace(r, c, total):  
            if 0 <= r < row and 0 <= c < col:
                total.append(dungeon[r][c])
                if (r, c) == (row - 1, col - 1):  
                    totals.append(total)
                    return
            else:
                return 

            trace(r, c + 1, total[:])            
            trace(r + 1, c, total[:])

        trace(0, 0, [])
        # print(totals)
        
        return len(totals), totals

c=3
r=3
print(Solution().calculateMinimumHP([[random.randint(-10, 10) for i in range(c)] for j in range(r)]))

import itertools, time
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row = len(matrix)
        col = len(matrix[0])
        coordinates = row * col
        ans = []        
        r = c = 0
        for x, y in itertools.cycle(direction):       
            while True: 
                time.sleep(1)
                if matrix[r][c] is not None:
                    ans.append(matrix[r][c])
                    matrix[r][c] = None
                print(*matrix, sep='\n', end="\n\n")
                if 0 <= r + x < row and 0 <= c + y < col and matrix[r + x][c + y] != None:                                     
                    r += x
                    c += y
                else:
                    break 
            if len(ans) == coordinates:
                break
        return ans    
    
print(Solution().spiralOrder([[2,5,9],[8,4,6],[0,-1,8]]))
    
print(Solution().spiralOrder([[1,2,3]*4,[4,5,6]*4,[7,8,9]*4,[4,5,6]*4,[4,5,6]*4]))

import os

class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def generateMatrix(self, m: int, n: int) -> list[list[int]]:
        matrix = [['   ' for i in range(n)] for j in range(m)]
        r = c = 0
        z = 1
        for x, y in itertools.cycle(self.directions):       
            while True: 
                if matrix[r][c] is '   ':
                    matrix[r][c] = f'{z:03d}'
                    os.system('cls')
                    print(*matrix, sep='\n', end='\n\n'), time.sleep(0.1)
                    z += 1
                if 0 <= r + x < m and 0 <= c + y < n and matrix[r + x][c + y] is '   ':                                     
                    r += x
                    c += y
                else:
                    break 
            if z == m * n + 1:
                break
        os.system('cls')
        return matrix 

# print(*Solution().generateMatrix(15, 15), sep='\n')


import time

def fibo(n):
    memo = {}
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]




def fib(n):
    if n <= 2:
        return 1
    return fibo(n-1) + fibo(n-2)

    
def f(n):
    memo = {}
    for i in range(1, n+1):
        if i <= 2:
            ans = 1
        else:
            ans= memo[i-1] + memo[i-2]
        memo[i] = ans
    return memo[n]

a = time.time()
print(f(35), time.time() - a)

a = time.time()
# print(fibo(35), time.time() - a)

a = time.time()
# print(fib(35), time.time() - a)

class Solution:
    minlength = float('inf')
    x = 1

    def removeword(self, wordlist, word):
        wordlist.remove(word)
        return wordlist

    def minExtraChar(self, s: str, dictionary: list[str]) -> int:          
        def check(string, worddict):
            self.x += 1
            for word in worddict:
                print(self.x, word, worddict)
                newstring = string.replace(word, '1')
                self.minlength = min(self.minlength, len(newstring.replace('1', '')))
                check(newstring, self.removeword(worddict.copy(), word))
        check(s, dictionary)
        return self.minlength



s = "dwmodizxvvbosxxw"
dictionary = ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]

s = "leetscode"
dictionary = ["et","code","leetcode", 's']
print(Solution().minExtraChar(s, dictionary))
import re
pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
print(re.match(pattern, "9.0.255.19"))
