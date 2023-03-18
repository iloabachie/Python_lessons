# create an empty adjacency list
adj_list = {}

# add three vertices to the graph
for i in range(1, 4):
    adj_list[i] = []

# add three edges to the graph
adj_list[1].append(2)
adj_list[2].append(3)
adj_list[3].append(1)

# print the adjacency list
print(adj_list)

# find the vertices adjacent to vertex 2
print(adj_list[2])

# add a new edge to the graph
adj_list[1].append(3)

# traverse the graph by visiting all of its vertices
visited = []
for vertex in adj_list:
    if vertex not in visited:
        visited.append(vertex)
        for neighbor in adj_list[vertex]:
            if neighbor not in visited:
                visited.append(neighbor)
print(visited)


def decimal_to_binary(n: int) -> str:
    # if the number is 0, return "0"
    if n == 0:
        return "0"
    
    # initialize the result as an empty string
    result = ""
    
    # keep dividing the number by 2 and adding the remainder
    # to the result until the number is 0
    while n > 0:
        result = str(n % 2) + result
        n //= 2
    
    # return the result as a string
    return result


def longest_palindrome(s: str) -> str:
    # if the string is empty, return an empty string
    if not s:
        return ""

    # initialize the longest palindrome to be the first character of the string
    longest = s[0]

    # loop through the string, starting at the second character
    for i in range(1, len(s)):
        # for each character, try to find the longest palindrome
        # centered at that character
        palindrome = get_palindrome(s, i, i)
        if len(palindrome) > len(longest):
            longest = palindrome

        # also try to find the longest palindrome centered between
        # the current character and the next character
        palindrome = get_palindrome(s, i, i + 1)
        if len(palindrome) > len(longest):
            longest = palindrome

    # return the longest palindrome
    return longest

# helper function to find the longest palindrome centered at or
# between the given indices
def get_palindrome(s: str, left: int, right: int) -> str:
    # while the left and right indices are valid and the characters
    # at those indices are the same, expand the palindrome on both sides
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    # return the palindrome, starting from the character just after the
    # left index and ending at the character just before the right index
    return s[left + 1:right]




def solve_sudoku(board):
  empty_spaces = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

  if not empty_spaces:
    return True

  for i, j in empty_spaces:
    for n in range(1, 10):
      if is_valid(board, i, j, n):
        board[i][j] = n
        if solve_sudoku(board):
          return True
        board[i][j] = 0

  return False

def is_valid(board, row, col, num):
  # Check if num is already in the row
  for i in range(9):
    if board[row][i] == num:
      return False

  # Check if num is already in the column
  for i in range(9):
    if board[i][col] == num:
      return False

  # Check if num is already in the 3x3 grid
  grid_x = row // 3
  grid_y = col // 3
  for i in range(grid_x * 3, grid_x * 3 + 3):
    for j in range(grid_y * 3, grid_y * 3 + 3):
      if board[i][j] == num:
        return False

  return True


def unique_quadruplets(nums, target):
    # Initialize a list to store the quadruplets
    quadruplets = []

    # Iterate over all possible quadruplets
    for a in range(len(nums)):
        for b in range(len(nums)):
            if b == a:
                continue
            for c in range(len(nums)):
                if c == a or c == b:
                    continue
                for d in range(len(nums)):
                    if d == a or d == b or d == c:
                        continue

                    # Check if the quadruplet satisfies the conditions
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        quadruplet = [nums[a], nums[b], nums[c], nums[d]]
                        quadruplet.sort()
                        if quadruplet not in quadruplets:
                            quadruplets.append(quadruplet)

    return quadruplets

# Test the function
nums = [1, 2, 3, 4, 5]
target = 9
print(unique_quadruplets(nums, target)) # Should print [[1, 2, 3, 3], [1, 2, 4, 2], [1, 3, 3, 2], [2, 2, 3, 2]]


my_dict = {
    'spider': 'photo',
    'aqua': 'swimmer',
    'iron': 'engineer'
}

new = {(key if key != 'iron' else 'bat') + 'man': value for key, value in my_dict.items()}
print(new)


from time import time
from random import randint

n = [1,2,3,4,5,6,7,8,9,0] * 900

def rotate(n, k):
    k = k % len(n)
    if k:    
        n =  n[-k:] + n[:len(n) - k]
        # print(len(n))
    else:
        # print(n)
        pass

def rotate2(n, k):
    for _ in range(k):
        n.insert(0, n.pop())
    # print(len(n))

for _ in range(10):
    k = randint(0, 10*len(n))
    start = time()
    rotate(n, k)
    slice = time() - start
    print(f'{k=}, {slice=}')
    
    start1 = time()
    rotate2(n, k)
    loop = time() - start1
    print(f'{k=}, {loop=}')
    print(f'**{slice=} - {loop=} = {(slice - loop)}')
    