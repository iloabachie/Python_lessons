from time import time
def fact(n):
    while n >= 1:
        return n * fact(n-1)
    else:
        return 1

start = time()
print(fact(50))
print(time() - start)


# fibonnacci recursion

def fib(n):
    while n >= 3:
          return (fib(n-1) + fib(n-2)) 
    else:
        return 1
    
fibs = []
for _ in range(10):
    fibs.append(fib(_))

print(fibs)

der = time()
print(fib(25), 'recursion:', time() - der)

#----fibonacci memoize----------------------

start = time()
def fibm(n, memo=[None]):

    if memo[n-1] is not None:
        return memo[n - 1]
    while n >= 3:
        result = fibm((n-1), memo) + fibm((n-2), memo) 
        memo[n-1] = result
        return result
    else:
        result = 1
        memo[0], memo[1] = 1, 1
        return result


n = 25
memo = [None] * n
print(fibm(n, memo), 'memoize:', time() - start)

#-- fibonnaci bottom up----------

star=time()
def bottom(n):
    memo = [None] * (n+1)
    
    memo[0], memo[1] = 1, 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n-1]

print(bottom(25), 'bottomup:', time() - star)

import sys

print(sys.getrecursionlimit())
print(sys.platform)

# print(vars(sys))
print(sys.argv)

import os
print(os.environ)

a = 5
b =  6

c = a
a = b
b = c





# a, b = b, a
print('a: ', a, 'b: ', b )
print([*'hello'])


# A simple generator function
def my_gen():    
    yield from 'helloes'

print(*my_gen())
print(*range(5))

# Using for loop
for item in my_gen():
    print(item)
    
    
    
    



class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        
node2 = TreeNode(3, 5, 6)
node3 = TreeNode(4)

node0 = TreeNode(8, node2, node3)

tree = node0

print(tree.key, tree.left.key, tree.right.key, tree.left.left, tree.right.right)