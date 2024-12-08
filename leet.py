def timer(funct):
    def wrapper(*args, **kwargs):
        from time import time
        start = time()
        funct(*args, **kwargs)
        print(f'{funct.__name__} ran in {time() - start} seconds')
    return wrapper

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

