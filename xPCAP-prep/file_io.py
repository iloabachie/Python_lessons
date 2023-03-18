# from os import strerror

# with open('.\\xPCAP-prep\\text.txt', 'w') as file:
#     file.write('''
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# ''')

# try:
#     counter = 0
#     stream = open('.\\xPCAP-prep\\text.txt', "rt")
#     # char = stream.readline(6)
#     # print(stream.readlines())
#     # print(stream.readlines(2))
#     # print(stream.readlines(2))
#     print('1', stream.readline())
#     print('2', stream.readline())
#     print('3', stream.readline())
#     # while char != '':
#     #     print(char, end='&')
#     #     counter += 1
#     #     char = stream.read(1)
#     #     print(char)
#     stream.close()
#     print("\n\nCharacters in file:", counter)
# except IOError as e:
#     print("I/O error occurred: ", strerror(e.errno))
    
    
    
# class A(object): pass
# class B(object): pass
# class C(object): pass
# class D(object): pass
# class E(object): pass
# class K1(A,B,C): pass
# class K2(D,B,E): pass
# class K3(D,A): pass
# k = K3()

# print(isinstance(k, (str, A, B, C, D, E)))

# print(K2.__mro__)


# F=type('Food',(),{'remember2buy':'spam', 'apple':'hello'})
# E=type('Eggs',(F,),{'remember2buy':'eggs'})
# G=type('GoodFood',(E,F),{})
# print('class e f g')
# print(F, E, G, "****")
# print('********', F.__name__, E.__name__, G.__name__)
# print(F.__dict__)

# obj = F()
# print(obj.apple)


# obj2 = G()

# print(issubclass(G, E))
# print(type(F), type(obj))


# print(G.__bases__)

# print('*******')


# p = float

# a = '6'

# b = p(a)

# print(type(p), b)

# print(type(int))

# a = type(int)

# a = dict(a='Geeks', b=2018)

# print(a['a'])

# print(type(obj2))

# -----------------------------------------------------

class Top:
    def __init__(self):
        self.a = print('top initialised')
        self.b = 'top'
        print('top initialised literal')
        
    def m_top(self):
        print("top function print")


class Middle():
    def __init__(self):
        self.d = print('middle initialised')
        self.b = 'middle'
        print('middle initialised lieteral')
        
    def m_middle(self):
        print("middle function print")


class Bottom(Middle):
    def __init__(self):
        
        self.c = print('bottom initialised')
        self.b = 'botom'
        print('bottom initialised literal')
        super().__init__()
        
    def m_bottom(self):
        print("bottom function print")

class Baby(Top, Bottom):
    def __init__(self):
        Top.__init__(self)
        Bottom.__init__(self)
        self.baby = 'baby initialised'
        
print(Baby.__mro__)

baby_obj = Baby()
# baby_obj.a


def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everything went fine")
    finally:
        print("It's time to say goodbye")
        return n


print(reciprocal(2))
print(reciprocal(0))

# print exception tree____________________________________________
def print_exception_tree(thisclass, nest=0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)


print_exception_tree(BaseException)


# ______________________________________________________________

def print_args(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))


try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ' ,end=' : ')
    print_args(e.args)

try:
    raise Exception("my exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

try:
    raise Exception("my", "exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)
	
 
 
 
two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y
 
for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))
    
    
print(two())

print(pwr(3, 6))


# ------------byte array-------------------------------------
data = bytearray(10)
print(len(bytearray(10)))

print(data[4])

for i in range(len(data)):
    data[i] = 10 * i

print(data, '|||||||', data[6])
for b in data:
    print(b, '||||', hex(b))
    
# --------------write byte array as binary file--------------

from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('xPCAP-prep\\file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# -------------------------------------------------------

from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


import calendar
print(calendar.calendar(2022))
print(calendar.month(2030, 8))

calendar.prcal(2030)

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst.args))
    for x in inst.args:
        print(x)
        

print(b'the quick brown fox'.translate(None, b'abcdefgh'))


def spam(x):
    y = 2
    def ham(z):
        return x + y + z
    return ham
 
for i in range(3):
    eggs = spam(i)
    print(eggs(i+3), end=' ')
    


a, b = 10, 20

print('\n', (lambda: a)(),lambda: b)
print((lambda: b, lambda: a)[False]())




# with open('xPCAP-prep\\spam.txt', 'r+') as file:
#     line = file.readline(5)
#     print((line), '*********************')
#     file.write(line)
#     file.writelines('hello wooo77777ooorld')
    
    

#---------------------------
# capture the output to console
print(88888888888888888888888888888888888888888888888888)
import sys

sys.stdout = open('xPCAP-prep\\spam.txt', 'a')  # redirects output to a file

print("This prints to file")
print(calendar.calendar(2022))
print(calendar.month(2030, 8))
print(calendar.month(2030, 3))

sys.stdout.close()
sys.stdout = sys.__stdout__  # redirects the output to the terminal

print("File saved")    
print(88888888888888888888888888888888888888888888888888)

for spam2 in open('xPCAP-prep\\spam2.txt'):
    print(spam2, end='')


print({False: 'No', 0: 'Nay', 0.0: 'Nope'})


x, y, z = "x", "y", "z"
s = [x, y, z]
t = x, y, z

print('/'.join(s), end="*")
print(t)


x = 3
while x > 0:
    print(x, end='')
    x //= 2
    
print()    
a, b = 10, 20
print(a < b and a or b)

print(10 or 20, 20 or 10)
print(10 and 20, 20 and 10)

print()
print(True and 10, 10 and True)
print(True or 10, 10 or True)


mylist = [1,2,3,4,5]

new = tuple(map(lambda x: x+1, mylist))

print(new)

int