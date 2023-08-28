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