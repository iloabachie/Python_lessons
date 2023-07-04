import random, timeit

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, value=None):        
        if value:
            self.root = Node(value)
        else:
            self.root = None
        
    def __contains(self, current_node, value):
        if not current_node:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self.__contains(current_node.left, value)
        if value > current_node.value:
            return self.__contains(current_node.right, value)
    
    def contains(self, value):
        return self.__contains(self.root, value)
        
    def __insert(self, current_node, value):
        if not current_node:
            return Node(value)
        if current_node.value > value:
            current_node.left = self.__insert(current_node.left, value)
        if current_node.value < value:
            current_node.right = self.__insert(current_node.right, value)
        return current_node
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__insert(self.root, value)
        
    def minimum(self):
        if not self.root:
            return None
        temp = self.root
        while temp.left:
            temp = temp.left
        return temp.value
    
    def __maximum(self, current_node):
        if not current_node.right:
            return current_node.value
        return self.__maximum(current_node.right)     
    
    def maximum(self):
        if not self.root:
            return None
        return self.__maximum(self.root)
    
    def delete(self, value):        
        ...  
    
    def count_nodes(self):  
        count = list()
        def counts(current_node): 
            if current_node:
                count.append(1)  
                if current_node.left:
                    counts(current_node.left)
                if current_node.right:
                    counts(current_node.right)  
        counts(self.root)   
        return sum(count)
                
    def count_nodes1(self):
        count = 0
        def counts(current_node, num): 
            nonlocal count
            count = num
            if current_node:
                count += 1
                if current_node.left:
                    counts(current_node.left, count)
                if current_node.right:
                    counts(current_node.right, count)  
        counts(self.root, count) 
        return count


my_bst = BinarySearchTree()

for _ in [random.randint(0, 50) for _ in range(35)]:
    my_bst.insert(_)

for _ in [random.randint(0, 50) for _ in range(20)]:
    print(_, my_bst.contains(_))


for _ in range(1, 50, 3):
    print(_, BinarySearchTree._BinarySearchTree__contains(my_bst, my_bst.root, _))
    
print(my_bst.minimum())
print(my_bst.maximum())

print("+++++++++++", my_bst._BinarySearchTree__maximum(my_bst.root))

print(type(my_bst), type(my_bst.root), type(my_bst.root.right))

print(BinarySearchTree.minimum(my_bst))
print(BinarySearchTree._BinarySearchTree__maximum(my_bst, my_bst.root.right.left))

print(my_bst.count_nodes1())



new_bst = BinarySearchTree()

print(new_bst.count_nodes1())

print(timeit.timeit(stmt=my_bst.count_nodes, number=1000000))
print(timeit.timeit(stmt=my_bst.count_nodes1, number=1000000))

print(sum(timeit.repeat(stmt=my_bst.count_nodes, repeat= 10, number=100000))/10)
print(sum(timeit.repeat(stmt=my_bst.count_nodes1, repeat= 10, number=100000))/10)