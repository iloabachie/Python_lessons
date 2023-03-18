def timer(funct):
    def wrapper(*args, **kwargs):
        from time import time
        start = time()
        funct(*args, **kwargs)
        print(f'{funct.__name__} ran in {time() - start} seconds')
    return wrapper




# https://leetcode.com/problems/divide-two-integers/

# ----------- does not satify all possibilities solution with >>
dividend = 7
divisor = 3

p, q = abs(dividend), abs(divisor)

i = 0
while q < p:
	i += 1
	q <<= 1
	print('*', p, q)

quotient = 1
q >>= 1
p -= q

for j in range(i - 1):
    q >>= 1
    quotient <<= 1
    print('quotient = ', quotient)
    if p >= q: 
        p -= q
        quotient += 1
if dividend * divisor < 0:
    quotient = -quotient
print(quotient)

# https://leetcode.com/problems/count-number-of-bad-pairs/

import collections

nums = [4,1,3,3]
nums = [1,2,3,4,5,6]
# nums = [8,4,9,7,1,0,4,6,3,3,5]
nums = [8,4,9,7,1,0,4,6,3,3,5]

p = [i - num for i, num in enumerate(nums)]
print("p = ", p)

q = collections.Counter(p)
print("q = ", q)
# print(type(q))

r = q.values()
z = q.keys()
print("r = ", r, z, end='###\n')
# print(type(r))

s = [x * (len(nums) - x) for x in r]
print("s = ", s)

ans = sum(s) // 2
print("one line ans = ", ans)

# one line solution-----------

bad_pairs = sum(x * (len(nums) - x) for x in collections.Counter(i - num for i, num in enumerate(nums)).values()) // 2
print(bad_pairs)


# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/


# https://leetcode.com/problems/maximal-square/description/
# Find area of largest square containing 1's
 
matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
    ]

matrix = [
    ["1","1","1","1","0"],
    ["1","1","1","1","0"],
    ["1","1","1","1","1"],
    ["1","1","1","1","1"],
    ["0","0","1","1","1"]
    ]

matrix = [
    ["1","0","1","1","0","1"],
    ["1","1","1","1","1","1"],
    ["0","1","1","0","1","1"],
    ["1","1","1","0","1","0"],
    ["0","1","1","1","1","1"],
    ["1","1","0","1","1","1"]
    ]

matrix = [['1'], ['1']]

num_columns = len(matrix[0])
num_rows = len(matrix)

for r in range(num_rows):
    for c in range(num_columns):     
        if c == 0 or r == 0 or matrix[r][c] == '0':
            matrix[r][c] = int(matrix[r][c])
        else:
            matrix[r][c] = 1 + min(int(matrix[r-1][c]), int(matrix[r][c-1]), int(matrix[r-1][c-1]))
    
lists = []
for lis in matrix:
    lists.append(max(lis))
    
area = max(lists)**2
print(area)


# https://leetcode.com/problems/zigzag-conversion/

phrase = 'PAYPALISHIRINGPAYPAIRINGPAYPALISHIRING'

def zigzag(word: str, row: int) -> str:
    index = [*range(row)]
    index = index + index[-2:0:-1]
    #-------------------------------------------
    # alternative way of enumerate but slow
    l = []
    nindex = list(index)
    for g in word:        
        l.append((nindex.pop(0), g))                   
        if not nindex:
            nindex = list(index)
    print(l)   
    
    # _----------------------------------------
    index = index * (len(word) // len(index) + 1)
    
    together = list(zip(index, list(word)))  # or [*zip(index, word_list))]
    new_string = ''
    
    for _ in range(len(together)):
        new_string += ''.join([y for x, y in together if x == _])
    print(new_string) 

zigzag(phrase, 5)      

# Compute crazy score using odd metrics

ops = ['-2', '5', '2', 'C', 'D', '+']
ops = ['2']
ops = ['5', '-2', '4', 'C', 'D', '9', '+', '+'] + [ '5', '2', 'C', 'D', '+']

result = []
for x in ops:
    if x == 'C':
        result = result[:-1]
        print(2, result)
    elif x == 'D':
        result.append(result[-1]*2)
        print(3, result)
    elif x == '+':
        new = sum(result[-2:])
        result.append(new)
        print(4, result)
    else:
        result.append(int(x))
        print(1, result)
print(result)
print(sum(result))



# https://leetcode.com/problems/longest-substring-without-repeating-characters/

import time

s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

start1 = time.time()
length = []
y = s
index = 0
while len(y):    
    y = s[index:] 
    word = ''
    for letter in y:
        if letter not in word:
            word += letter        
        else:
            break
    length.append(len(word))
    index += 1
          
print(max(length) if len(s) != 0 else 0)
print(index, time.time() - start1)



# https://leetcode.com/problems/longest-palindromic-substring/submissions/

s = "crbidxnkyieminyzchamldzjzglygkfbbyggagwdqdqamzpguppqjfrcewfduwvcmhliahovcwoupwxwhaoiiiguahuqxiqndwxqxweppcbeoasgtucyqlxnxpvtepwretywgjigjjuxsrbwucatffkrqyfkesakglyhpmtewfknevopxljgcttoqonxpdtzbccpyvttuaisrhdauyjyxgquinvqvfvzgusyxuqkyoklwslljbimbgznpvkdxmakqwwveqrpoiabmiegoyzuyoignfcgmqxvpcmldivknulqbpyxjuvyhrzcsgiusdhsogftokekbdynmksyebsnzbxjxfvwamccphzzlzuvotvubqvhmusdtwvlsnbqwqhqcigmlfoupnqcxdyflpgodnoqaqfekhcyxythaiqxzkahfnblyiznlqkbithmhhytzpcbkwicstapygjpjzvrjcombyrmhcusqtslzdyiiyvujnrxvkrwffwxtmdqqrawtvayiskcnpyociwkeopardpjeyuymipekbefbdfuybfvgzfkjtvurfkopatvusticwbtxdtfifgklpmjamiocalcocqwdivyulupammxhdbeazrrktxiyothnvbwwrsocxzxaxmoenigbhvxffddexrwsioqoyovaqvtmkwzupstkgkmvrddzolmuzjnsj"

s = '''
1520-2791,2842, 3351-3836,4214-4225,4812,4814,4816,4899-5013, 5039, 5047-5085, 5099,5137-5139,5172-5251,5300, 5310,5399-5411, 5441, 5511-5542, 5691, 5811-5812, 5814,5941-5942,5964, 5969-5970,5992, 7011, 7296,7332-7349,7393-7511,7524-7534, 7549,7692-7699, 7829-7832,7929, 7933-7941, 7991, 7996, 8011, 8398-8641, 8699-8734, 8999,9222,9399,

0742-3090,3094-5085, 5099-5310, 5331-5661, 5691-5722,5733-5815,5817-5932,5935 -5943,5946-5999,6050-7261, 7276,7278-7296, 7298-7321,7332-7699, 7829-7994, 7996- 8641,8675-9222,9311-9399,9402-9752,9950,

0742-3090,3094-5085, 5099-5310,5331-5661,5691-5722,5733-5815,5817-5932,5935 - 5943,5946-5999, 6050-7261,7276,7278-7296, 7298-7321,7332-7699,7829-7994,7996- 8641,8675-9222,9311-9399,9402-9752,9950,
'''

print('solutuionn')

start = time.time()

word = []
count = 0
for p in range(len(s)):  
    for q in range(len(s),0,-1):  
        if p < q and s[p:q] == s[p:q][::-1]: # runs faster without the first condition.
            # print(p,q)
            word.append(s[p:q])
            count+=1
            break

max = 0
for _ in word:
    max = len(_) if len(_) > max else max
wordlist = [x for x in word if len(x) == max]
print(wordlist[0], end='  '), print(count)
            
    
print(time.time() - start)



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
tree = TreeNode(
    10, 
    TreeNode(5, 
             TreeNode(3, 
                         TreeNode(3), 
                         TreeNode(-2)
                         ), 
             TreeNode(2, 
                      None, 
                      TreeNode(1)
                      )
             ),
    TreeNode(-3, 
             None, 
             TreeNode(11)
             )
    )

@timer
def pathSum(root, targetSum):
    def count(root, path):
        if root:
            if not root.left and not root.right:
                path.append(root.val)
                yield path
            for _ in count(root.right, path + [root.val]):
                yield _
            for _ in count(root.left, path + [root.val]):
                yield _
                
    for x in [*count(root, [])]:
        print(x)
    print("End of all nodd pathsums of length " + f'{len([*count(root, [])])}')
        
    paths = [*count(root, [])]
    
    x = 0
    for _ in paths:
        for p in range(len(_)):
            for q in range(len(_),-1,-1):
                if p <= q:
                    if sum(_[p:q]) == targetSum:
                        print(_, _[p:q])
                        x += 1
    print(x)
    
pathSum(tree, 8)

# Create binary tree
import random

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# create a binary tree...
def generate_tree(num_nodes):
    if num_nodes == 0:
        return None
    value = random.randint(1, num_nodes)
    left_size = random.randint(0, num_nodes - 1)
    right_size = num_nodes - 1 - left_size
    return Node(value, generate_tree(left_size), generate_tree(right_size))

node = generate_tree(90000)  # generate a binary tree with 1000 nodes


# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

def speed_calc_decorator(funct):
    def wrapper(*args, **kwargs):
        current_time = time.time()
        funct(*args, **kwargs)
        print(f'{funct.__name__} run speed: {time.time() - current_time}')
    return wrapper

@speed_calc_decorator
def preorderTraversalme(root): # -> List[int]:
    def preorder(root):
        if root:
            yield root.val
            for _ in preorder(root.left):
                yield _
            for _ in preorder(root.right):
                yield _
    print('111111', len([*preorder(root)]))

@speed_calc_decorator
def preorderTraversal(root):
    def pre(root):
        preord = []
        if root:
            preord.append(root.val)
            preord += pre(root.left)
            preord += pre(root.right)
        return preord
    pre(root)

@speed_calc_decorator
def preorder_iterative(root):
    if not root:
        return
    stack = [root]
    preord = []
    while stack:
        node = stack.pop()
        preord.append(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    print(22222, len(preord))

preorderTraversalme(node)
preorderTraversal(node)
preorder_iterative(node)

# https://leetcode.com/problems/same-tree/solutions/32729/shortest-simplest-python/?orderBy=most_votes

def isSameTree(self, p, q):
    if p and q:
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    return p is q

# Method 2

def isSameTree(self, p, q):
    def t(n):
        return n and (n.val, t(n.left), t(n.right))
    return t(p) == t(q)

# Method 3

def isSameTree(self, p, q):
    return p and q and p.val == q.val and all(map(self.isSameTree, (p.left, p.right), (q.left, q.right))) or p is q


# Straight forward

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
            

# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/submissions/894434220/

from operator import itemgetter

y = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]

def kWeakestRows(mat, k: int):        
               
    return [*map(itemgetter(0), sorted(enumerate([sum(_) for _ in mat]), key=itemgetter(1)))][:k]


print(kWeakestRows(y, 3))        