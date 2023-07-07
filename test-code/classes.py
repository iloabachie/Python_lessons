lists = [1, 3, 2, 4, 1, 2, 3, 4, 5]

dicttionary = dict.fromkeys(lists)
# dicttionary = list(vars())
print('2', dicttionary)
new_list = list(dicttionary)
print('3', new_list)

print('-----------------------')


# # -------------------------------------
class Animal:
    def __init__(self):
        self.eyes = 2
        self.legs = 4
        self.tail = True
    
    def move(self):
        print('this animal moves superclass')
    
    def feel(self):
        print('this animal feels superclass')


class Dog1(Animal):
    def __init__(self):
        super().__init__()
        self.skin = 'hairy'

    def speak(self):
        print('bark bark')
    
    def move1(self):
        # Animal.move(self)
        print('runs on 4 legs form subclass')

suzy = Dog1()

print(suzy.skin)
print(suzy.legs)
print(suzy.eyes)

suzy.move()
suzy.feel()
suzy.speak()


# # ------------------------------------
# class Dog:
#     def __init__(self):
#         self.temperament = "loyal"
 
# class Labrador(Dog):
#     def __init__(self):
#         super().__init__()
#         self.temperament = "gentle"

# doggo = Dog()
# print(f"A dog is {doggo.temperament}")
 
# sparky = Labrador()
# print(f"Sparky is {sparky.temperament}")


# from collections import Counter


# a = 'dsfksdkfasdow409wetoidfgpo3487t934759843598y4uh54h'

# my_counter = Counter(a)

# print(my_counter)

import timeit
print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))

print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))

print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))

# one = "#".join(str(n) for n in range(5))

# two = "$".join([str(n) for n in range(5)])

# three = "-".join(map(str, range(5)))

# print(one, two, three)

# check = map(str, range(6))
# print(check)
# print(list(check))

# check = map(str, range(6))
# print(check)
# print(list(check))

# import time
# import random

# for _ in range(15):
#     print("every 5 seconds something shoulld appear")
#     # time.sleep(1)
#     print(random.randint(-270, 270))



#find the longest palindrome in the word.

# with open('high_score.txt') as file:
#     high_score = file.read()
# print(high_score)

# with open('high_score.txt', mode='a') as file:
#     file.write(f'{high_score}')



# hi = [2,4,5,6,7,8,9,0,0,8,7,6]
# double = []
# for _ in hi:
#     double.append(_*2)

# print(2, double)
# triple = []
# for n in hi:
#     triple.append(n*3)

# print(3, triple)

# import random

# print(random.random())


seasons = ['Spring', 'Summer', 'Fall', 'Winter']
def enumerat(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
    
for i, j in enumerat(seasons):
    print(i, j)
# dict comprehension

weather_c = {
    'Monday': 22,
    'Tuesday': 33,
    'Wednesday': 25,
    'Thursday': 14,
    'Friday': 23,
    'Saturday': 7
}

weather_f = {item: (c * 5 / 9 + 32) for item, c in weather_c.items() if c % 2 == 0}

print(weather_f)

print("****", weather_c.items())



def permute(string, pocket=''):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket)
            
permute('ABC', '')

import pdb
from tkinter import Y
print(dir(pdb))

import collections

print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print(collections.Counter({'a':2, 'b':3, 'c':1}))
print(collections.Counter(a=2, b=3, c=1))

c = collections.Counter('abcdaab')

for letter in 'abcde':
    print(f'{letter} : {c[letter]}')

c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabetaa')

print('C1:', c1)
print('C2:', c2)

print('\nCombined counts:')
print(c1 + c2)

print('\nSubtraction:')
print(c1 - c2)

print('\nIntersection (taking positive minimums):')
print(c1 & c2)

print('\nUnion (taking maximums):')
print(c1 | c2)


def square(nums: list):
    for _ in nums:
        x = _**2
        yield x



sq = square([1, 2, 3, 4, 5])

# print(list(sq))
# print(next(sq), next(sq), next(sq), next(sq), next(sq))
# # print(next(sq))
# # print(next(sq))
# # print(next(sq))
# # print(next(sq))


print(next(sq) + next(sq))

def pop(list):
    def get_last(my_list):
        return my_list[len(my_list)-1]
    list.remove(get_last(list))
    return list

a = [1,2,3,4,5,6]
a.remove(4)
print(pop(a))
print(pop(a))
print(pop(a))


def nth_power(exponent):
    def powerof(num):
        return pow(num, exponent)
    return powerof


cube = nth_power(3)(999)

print(cube)

squ = nth_power(2)

print(squ(16))


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

 


print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

for x in "00123dfgh65478900":
    try:
        print(int(x))
    except ValueError:
        print(x)
        
def add(*args):
    y = 0
    for n in args:
        y += n
    return y

z = add(5,6,9,7,3,40,25)

print(z)


def calculate(n, **kwargs):
    n *= float(kwargs.get('x'))
    n += float(kwargs.get('pl'))
    print(n)
    
calculate(3, pl=3, x=6)


i = 3
while i > 0:
    i -= 2
    print('*')
    if i == 2:
        break
else:
 
    print('*mmm')
    
try:
    print('try' + "try")
except NameError as error:
    print('except')
    print(error)
    
else:
    print('else')
finally:
    print('finally')

print(''.join(sorted('32sdfgsdfg1')))

tem  = list('321')
tem.sort()

print(tem)

try:
    print(5/0)

except (ValueError, ZeroDivisionError):
    print("Too bad...")
except SyntaxError:
    print("Sorry, something went wrong...")
    
    
d = {}
d[1] = 1
d['hi'] = 2
d[1] += 1

print(d)
 
sum = 0
 
for k in d:
    print(k)
    sum += d[k]
 
print(sum)

# num = 1
 
 
def func():
    # num = 1
    # global num
    num = 1
    num = num + 3
    print(num)
 
 
func()
 
class Cat:
    Species = 1
 
    def get_species(self):
        return 'kitty'
 
 
class Tiger(Cat):
    def get_species(self):
        return 'tiggy'
 
    def set_species(self):
        pass
 
 
creature = Tiger()
print(hasattr(creature, "Species"),
      hasattr(Cat, "set_species"))


# check in thonny
# x = [0, 1, 2]
# x.insert(0, 1)
# print(x)
# del x[1]
# print(x)
# print(sum(x))

x = True
y = False
z = False
 
if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)


x = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
 
def func(data):
    res = data[0][0]
    for da in data:
        for d in da:
            if res < d:
                res = d
    return res
 
print(func(x[0]))

print(len([i for i in range(-1, -2)]))

import math
 
result = math.e != math.pow(2, 4)
print(int(result))


list1 = [1, 3]
list2 = list1
list1[0] = 4
print(list2)

def func(x):
    return 1 if x % 2 != 0 else 2
 
 
print(func(func(1)))

active_list = [123, 456, 789, 159]

code = 123

{code} if {len(str(code)) == 4} else f'0{code}'

print(f'{code} unblocked' if code in active_list else f'{code} blocked')

print(1 if 1==1 else 0.5 if 2>1 else 1)


import random

print(type(print(type(type(type('hello'))))))

print('hello'.__class__)

print(random.random() - random.random())

print(0**0)

t = '%(a)s %(b)s %(c)s'
print(t % dict(a='Welcome', b='to', c='Turing'))

class Developer:
    def __init__(self):
        self.__seniority = 'Junior'
        self.skills = '88'

    def display(self):

        print('Welcome to Turing with {seniority} developer with skill {skills}'.format(seniority=self.__seniority, skills=self.skills))

class NodeJS(Developer):
    def __init__(self):
        super().__init__() 
        self.__seniority = 'Senior'
        self.skills = 'NodeJS'

c = NodeJS() 
c.display()


print(c)
# print(c._Developer__seniority)
# print(c.skills)

import re
result = re.findall("Welcome to Turing", 'Welcome;, 1')
print(result)



# -------------------------------------------------
# how to time a function using decorators

def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        __ = func(*args, **kwargs)
        total = time.time() - start
        print('Total runtime: ', total)
        return __
    return wrapper

@timer
def forloop():
    y = [x for x in range(99999999) if x % 57559 == 3 and x % 48596 == 16]
    print('Comprehension', y)
    return y
        
@timer
def forloop2():
    x = []
    for y in range(99999999):
         if y % 57559 == 3 and y % 48596 == 16:
             x.append(y)
    print('For loop', x)
    return x

# forloop()
# pppp = forloop2()

# forloop = timer(forloop)

# forloop()    

# print('[[[', pppp)
# -------------------------------------------------------


phrase = 'PAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRIN'

@timer
def zigzag(word: str, row: int) -> str:
    index = [_ for _ in range(row)]
    index = index + index[-2:0:-1] 
    index = index * (len(word) // len(index) + 1)
    word_list = list(word)
    together = list(zip(index, word_list))
    new_string = []
    
    for _ in range(len(together)):
        new_string += [y for x, y in together if x == _]
        
    print('zigzag:', ''.join(new_string) if len(''.join(new_string)) < 20 else 'time test')
    
       
zigzag(phrase, 5)  

@timer
def zigzags(word: str, row: int) -> str:
    index = [_ for _ in range(row)]
    index = index + (index[::-1])[1:-1]
    index = index * (len(word) // len(index) + 1)
    word_list = list(word)
    together = list(zip(index, word_list))
    new_string = []
    
    for _ in range(len(together)):
        new_string += [y for x, y in together if x == _]
        
    print('zigzags:', ''.join(new_string) if len(''.join(new_string)) < 20 else 'time test')


# zigzag(phrase, 5)     
# zigzags(phrase, 5)  
# zigzag(phrase, 5)     
# zigzags(phrase, 5)  
# zigzag(phrase, 5)     
# zigzags(phrase, 5)  
# zigzag(phrase, 5)     
# zigzags(phrase, 5)  


data = ['a', 'b', 'c', 'd']

import copy
newlist = data.copy()


print(newlist)

print(id(newlist), id(data))

# print(vars(copy))


class A:
    def __init__(self):
        print("Initializing A")

class B:
    def __init__(self):
        print("Initializing B")

class C(A, B):
    def __init__(self):
        super(B, self).__init__()  # Initializing only the B superclass
        print("Initializing C")
        # B.__init__(self)
        # A.__init__(self)

c = C()
print("end")

class A:
    def __init__(self):
        print("Initializing A")

class B:
    def __init__(self):
        print("Initializing B")

class C:
    def __init__(self):
        print("Initializing C")

class D(A, B, C):
    def __init__(self):
        super().__init__() 
        super().__init__() 
        print("Initializing D")
        # B.__init__(self)
        # A.__init__(self)
        # C.__init__(self)

d = D()
print(type(D.__mro__))
print(D.__mro__)


class A:
    def __init__(self):
        print("Initializing A")

class B(A):
    def __init__(self):
        super(B, self).__init__()  # Initializing only the B superclass
        print("Initializing B")

class C(A):
    def __init__(self):
        super(C, self).__init__()  # Initializing only the C superclass
        print("Initializing C")

class D(B, C):
    def __init__(self):
        print("start")
        super(B, self).__init__()  # Initializing only the B superclass
        super(C, self).__init__()  # Initializing only the C superclass
        print("Initializing D")



# c = C()
d = D()
print(D.__mro__)

import sys
print(sys.implementation)#, 

print(sys.getwindowsversion())#, sys.implementation, sys.stdout)