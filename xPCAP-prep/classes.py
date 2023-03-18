# def f(t):
#     def g(t):
#         def h():
#             nonlocal t
#             t += 1
#             print(1)
#         return h, lambda: t
#     h, gt = g(0)
#     print(2)
#     return h, gt, lambda: t

# h, gt, ft = f(0)
# ft(), gt()
# h()
# ft(), gt()

# def a():
#     print('a')


# c, b = a()

# print(c, b)


test = 'donor'
longer = 'nabucodonosor'


print('No' if [*filter(lambda x: x not in longer, test)] else 'Yes')


if 1: print(11) 
else: print(12)


a: str

a = input("enter value: ")
print(a)

a = 2

print(a)

class Control:
    #def __init__(self):
    my_ID = 1
 
    def say(self):
        return self.my_ID
        

class SubClass(Control):
    def __init__(self):
	    #super().__init__()
        pass
        
print('*******', issubclass(SubClass, Control))
x = 1        
        
new_object = SubClass()
print(new_object.my_ID)

print(isinstance(new_object, SubClass))


class Storage:
    def __init__(self):
        self.rack = 1
 
    def get(self):
        return self.rack
 
    def print(self):
        # Insert a method here
        print(Storage.get(self))
 
 
stuff = Storage()
print(stuff.print())

i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print('*')
    
    
print(type(print("hello")))


# ---------------------------------


# defining class A
class A:
    def __init__(self, txt):
        print(txt, 'I am in A Class')
  
# B class inheriting A
class B(A):
    def __init__(self, txt):
        print(txt, 'I am in B class')
        super().__init__(txt)
      
# C class inheriting B
class C(B):
    def __init__(self, txt):
        print(txt, 'I am in C class')
        super().__init__(txt)
  
# D class inheriting B
class D(B):
    def __init__(self, txt):
        print(txt, 'I am in D class')
        super().__init__(txt)
  
# E class inheriting both D and C
class E(C, D):
    def __init__(self):
        print( 'I am in E class')
        super().__init__("hello")
  
# driver code
d = E()
print('')
h = C('hi')