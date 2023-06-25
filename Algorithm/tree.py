# Binary Search Tree

class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

#=========================================================
#creates the first node 
class BinarySearchTreeConstructor:
    def __init__(self, value):
        new_node = BinarySearchTreeNode(value)
        self.root = new_node
tree = BinarySearchTreeConstructor(57)
#=========================================================

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = BinarySearchTreeNode(value)
        if self.root == None:
            self.root = new_node
            return True        
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contains(self, value):
        temp = self.root
        while temp is not None:            
            if value == temp.value:
                return True
            if value < temp.value:
                temp = temp.left
            else: 
                temp = temp.right  
        return False


 

my_tree = BinarySearchTree()

import random
for _ in range(100):
    my_tree.insert(random.randint(0,100))

print(my_tree.root.right.right.left.value)

print(my_tree.contains(45))

