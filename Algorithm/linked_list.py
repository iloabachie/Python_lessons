from timeit import timeit

class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = self.tail = new_node
        self.length = 1
    
    def append_val(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1   
        return True 
        
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def print_vals(self):
        temp = self.head
        print("head->", end="")
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("<-tail")
    
    def linked_to_list(self):
        vals = []
        temp = self.head        
        while temp:
            vals.append(temp.value)
            temp = temp.next
        return vals
    
    def reversed_linked(self):
        if self.length in [0, 1]:
            return self
        reverse_list = self.linked_to_list()[::-1]
        new_linked_list = LinkedList(reverse_list[0])        
        for _ in reverse_list[1:]:
            new_linked_list.append_val(_)
        return new_linked_list 
    
    def reverse_in_place(self):
        temp = self.head        
        self.head, self.tail = self.tail, self.head
        prev = None  
        while temp:
            after = temp.next
            temp.next, prev = prev, temp               
            temp = after     
        
    def pop_first(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            temp = self.head
            self.head = self.tail = None
            self.length -= 1
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            return temp
        
    def pop_last(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            temp = self.head
            self.head = self.tail = None
            self.length -= 1
            return temp
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            popped = temp.next
            temp.next = None
            self.tail = temp
            self.length -= 1
            return popped
                
    def remove(self, index):
        if index == 0:
            return self.pop_first()  
        if index < 0 or index >= self.length or self.head is None:
            return None                   
        if index == self.length - 1:
            return self.pop_last()        
        temp = self.head
        for _ in range(index):  # use the get method next time
            hold = temp
            temp = temp.next
        hold.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
           
    def insert(self, index, value):                    
        if index == 0:
            return self.prepend(value)            
        if index < 0 or index > self.length:
            return False  
        if index == (self.length):
            return self.append_val(value)             
        temp = self.head
        new_node = Node(value)
        temp = self.get(index -1)
        new_node.next = temp.next
        temp.next = new_node        
        self.length += 1
        return True
        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp            
     
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def clear(self):
        self.head = self.tail = None
        self.length = 0 
 
    def rotate(self, k):
        if not self.head or not self.head.next or k == 0:
            return
        elif k > 0:
            for _ in range(k):
                self.tail.next = self.head
                self.head.prev = self.tail
                self.head = self.head.next
                self.head.prev = None
                self.tail = self.tail.next
                self.tail.next = None
                print(f'{self.head.value= }')
        else:
            k = abs(k)
            for _ in range(k):
                self.head.prev = self.tail
                self.tail.next = self.head
                self.tail = self.tail.prev
                self.tail.next = None
                self.head = self.head.prev
                self.head.prev = None
# ============================================

my_linked_list = LinkedList(10)

for _ in range(3,30, 7):
    my_linked_list.append_val(_)  

for _ in "linked_list":
    my_linked_list.append_val(_)  
    
my_linked_list.print_vals()

my_linked_list.set_value(8, "ant")

my_linked_list.print_vals()
print(my_linked_list.length)

print(my_linked_list.linked_to_list())

reverse = my_linked_list.reversed_linked()

reverse.print_vals()
print("prepend 222")
reverse.prepend(222)
reverse.print_vals()
a = reverse.pop_first()
reverse.print_vals()
print("======", a, a.value, a.next)

reverse.print_vals()
print(reverse.length)

a = reverse.pop_last()

print(a, a.value)

reverse.print_vals()

for _ in range(reverse.length):
    reverse.pop_last()
    reverse.print_vals()
    
my_linked_list = LinkedList(10)

for _ in "linked_list":
    my_linked_list.append_val(_)  

my_linked_list.clear()
    
my_linked_list.print_vals()

for _ in "how are you"[::-1]:
    my_linked_list.insert(0, _) 
    my_linked_list.insert(1, _*2) 
    my_linked_list.print_vals()

my_linked_list.prepend(22)
my_linked_list.prepend(23)
my_linked_list.prepend(24)
my_linked_list.print_vals()

print("++++++++++++++++++++++")
my_linked_list.print_vals()
a = my_linked_list.reverse_in_place()
my_linked_list.print_vals()
print(a)

print(timeit(stmt=my_linked_list.reversed_linked, number=100000))
print(timeit(stmt=my_linked_list.reverse_in_place, number=100000))

for _ in range(4):
    my_linked_list.reverse_in_place()
    my_linked_list.print_vals()

my_linked_list.rotate(13)
my_linked_list.clear()
my_linked_list.print_vals()


print("compare linked append and list append")

def linkedappend():
    new = LinkedList(1)
    for _ in range(100):
        new.append_val(_)
        
def listappend():
    new = [1]
    for _ in range(100):
        new.append(_)
        
        
print(timeit(stmt=linkedappend, number=100000))
print(timeit(stmt=listappend, number=100000))