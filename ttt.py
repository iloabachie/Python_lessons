import random
import math
import copy
from ttu import nums as C
import collections
import timeit


class A:
    def __init__(self):
        print("Initializing A")


class B:
    def __init__(self):
        print("Initializing B")


class C(A, B):
    def __init__(self):
        super().__init__()  # should initialize the B superclass
        print("Initializing C")
        B.__init__(self)


c = C()

print(11111111111)

C.__init__(c)


class Solution1:
    def countNegatives(self) -> int:
        grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
        if grid[-1][-1] >= 0:
            return 0

        # I could do binary search, but I'd rather do a simpler algorithm
        row, col = 0, len(grid[0])-1
        while grid[row][col] >= 0 and row < len(grid):
            row += 1

        # We are now at the rightmost cell in the first row containing negative values
        ans = 0
        while row < len(grid):
            while grid[row][col] < 0 and col >= 0:
                col -= 1
            if col < 0:
                break
            ans += len(grid[row]) - col - 1
            # print(f"ans: {ans}, row: {row}, col: {col}")
            row += 1

        # Since the first column of the current row is negative, just tally up the remaining cells
        #   Assume each row has the same size
        ans += (len(grid) - row) * len(grid[0])
        return ans


grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]


class Solution2:
    def countNegatives(self) -> int:
        return sum([len([y for y in x if y < 0]) for x in grid])


class Solution3:
    def countNegatives(self) -> int:
        for index, value in enumerate(grid):
            grid[index] = len([x for x in value if x < 0])
        return sum(grid)


class Solution4:
    def countNegatives(self) -> int:
        for index, value in enumerate(grid):
            grid[index] = len([*filter(lambda y: y < 0, value)])
        return sum(grid)


class Solution5:
    def countNegatives(self) -> int:
        return sum([len([*filter(lambda y: y < 0, x)]) for x in grid])


# print(timeit.timeit(stmt=Solution1().countNegatives))
# print(timeit.timeit(stmt=Solution2().countNegatives))
# print(timeit.timeit(stmt=Solution3().countNegatives))
# print(timeit.timeit(stmt=Solution4().countNegatives))
# print(timeit.timeit(stmt=Solution5().countNegatives))


class Solution1:
    def topKFrequent(self) -> list[int]:
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        return [x for x, y in collections.Counter(nums).most_common(k)]


class Solution2:
    def topKFrequent(self) -> list[int]:
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        return [x[0] for x in collections.Counter(nums).most_common(k)]


print("\ncounter")
# print(timeit.timeit(stmt=Solution1().topKFrequent))
# print(timeit.timeit(stmt=Solution2().topKFrequent))


nums = [random.randint(1, 30) for x in range(15)]


class Solution1:
    def productExceptSelf(self) -> list[int]:
        if nums.count(0) > 1:
            return [0] * len(nums)
        product = 1
        for i in nums:
            if i != 0:
                product *= i
        if nums.count(0) == 1:
            return [0 if x != 0 else product for x in nums]
        return [int(product/x) for x in nums]


class Solution2:
    def productExceptSelf(self) -> list[int]:
        if nums.count(0) > 1:
            return [0] * len(nums)
        product = math.prod(filter(lambda x: x != 0, nums))
        if nums.count(0) == 1:
            return [0 if x != 0 else product for x in nums]
        return [int(product/x) for x in nums]


print("\nnext")
# print(timeit.timeit(stmt=Solution1().productExceptSelf))
# print(timeit.timeit(stmt=Solution2().productExceptSelf))

from ttu import nums as C

class Solution1:
    def maxProduct(self) -> int:
        A = copy.deepcopy(C)
        B = A[::-1]
        for i in range(1, len(A)):
            # print(A, A[i], A[i - 1] or 1)
            # print(B, B[i], B[i - 1] or 1)
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
            # print(A)
            # print(B)
            # print("----")
        return max(A + B)


class Solution2:
    def maxProduct(self) -> int:
        A = copy.deepcopy(C)
        n = len(A)
        max_product = [A[0]]*n
        min_product = [A[0]]*n

        for i in range(1, n):
            max_product[i] = max(A[i], max_product[i-1] *
                                 A[i], min_product[i-1]*A[i])
            min_product[i] = min(A[i], max_product[i-1] *
                                 A[i], min_product[i-1]*A[i])

        return max(max_product)


class Solution3:
    def maxProduct(self) -> int:
        A = copy.deepcopy(C)
        n = len(A)
        max_product = [A[0]]*n
        min_product = [A[0]]*n

        for i in range(1, n):
            max_product[i] = max(
                (entity := (A[i], max_product[i-1]*A[i], min_product[i-1]*A[i])))
            min_product[i] = min(entity)

        return max(max_product)


# print(timeit.timeit(stmt=Solution1().maxProduct, number=1000))
# print(timeit.timeit(stmt=Solution2().maxProduct, number=1000))
# print(timeit.timeit(stmt=Solution3().maxProduct, number=1000))


target = 8
nums = [0,0,0,0,1,2,3,3,4,5,6,6,7,8,8,8,9,9,10,10,11,11]
class Solution1:
    def searchRange(self):
        
        if target not in nums:
            return [-1, -1]        
        return [nums.index(target), len(nums) - [*reversed(nums)].index(target) -1]
    
class Solution2:
    def searchRange(self):
        if target not in nums:
            return [-1, -1]        
        return [nums.index(target), len(nums) - nums[::-1].index(target) -1]



# print(timeit.timeit(stmt=Solution1().searchRange, number=1000000))
# print(timeit.timeit(stmt=Solution2().searchRange, number=1000000))


class MyClass:
    """This is a sample class."""

    def __init__(self):
        """This is the constructor method."""
        self.attribute = "Sample attribute"

    def my_method(self):
        """This is a sample method."""
        print("Hello, World!")

# Using help() with the class
# help(MyClass)

# help(Solution1)

help(Solution2().searchRange)


class Solution:
    def projectionArea(self, grid) -> int:
        # ans =int()
        # for i in range((l:=len(grid))):
        #     tallesti = tallestj = 0
        #     for j in range(l):
        #         print(i,j)
        #         if grid[i][j]:
        #             ans += 1
        #         tallesti = max(tallesti, grid[i][j])
        #         tallestj = max(tallestj, grid[i][j])
        #     ans += tallesti + tallestj
        



        # ans = sum(map(max, grid))
        # ans += sum(map(max, zip(*grid)))
        # ans += sum(v > 0 for row in grid for v in row)
        # print([v > 0 for row in grid for v in row])
        ...



#  transpose without zip function.       
from random import randint  
'''
grid = 
[r=[c,c,c,c,c],
 r=[c,c,c,c,c],
 r=[c,c,c,c,c],
 r=[c,c,c,c,c],
]
'''

def create_grid(row=None, col=None, fillval=None):
    from random import randint  
    if not row: row = randint(8,20) 
    if not col: col = randint(8,20) 
    grid = []
    for i in range(row):
        grid.append([])
        for j in range(col):
            grid[i].append(fillval if fillval else randint(0, 20))
    return grid

def transpose(grid):
    #col length transpose = row length original and versa for row length
    col = len(grid)
    row = len(grid[0])
    transpose = []
    for i in range(row):
        transpose.append([])
        for j in range(col):
            transpose[i].append(grid[j][i])    
    return transpose

def transpose1():
    return list(zip(*grid))


grid = create_grid(2,3)
print(grid)
transp = transpose(grid)
print(transp)


# for row in grid:
#     for col in row:
#         print(col)
a = [str(col) for row in grid for col in row]
print(a)

print([[str(col) for col in row] for row in grid])

import itertools
def largestTriangleArea(self, p):
    return max(0.5 * abs(i[0] * j[1] + j[0] * k[1] + k[0] * i[1]- j[0] * i[1] - k[0] * j[1] - i[0] * k[1]) for i, j, k in itertools.combinations(p, 3))


print([itertools.combinations('abcdefgh', 3)])

