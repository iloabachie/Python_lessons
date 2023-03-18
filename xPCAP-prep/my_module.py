
print('I am inside the file: ', __name__)


 
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
    if x < 18:
        return False
    else:
        return True
    
    
print('****************************testing filter functions')
adults = filter(myFunc, ages)

# why does the value of adults not hold after printing to console with one of hte following.
# for x in adults:
#  print(x)

print(list(adults))

# for x in adults:
#   print(x)


print(11111111111111111, list(adults))
print(222222222222222222222, (adults))
print(33333333333333333333333333, (adults))
print(444444444444444444444, (adults))

print('*************************testing map functions')


second = map(myFunc, ages)
# for x in second:
#   print(x)

print(list(second))
print(list(second))
print(list(second))
print(list(second))


print('****************************testing generator functions')
def genar():
    for x in range(8):
        yield x
        
        
        
generato = genar()

print(generato)
a =list(generato)
print('88888', list(generato))
print('8888', list(generato))
print('******', list(generato))
print(a)

for x in generato:
    print(x)
    
from random import seed, randint

# seed('ezue')
data = [randint(-10,10) for x in range(10)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)



import os
 
# os.mkdir('pictures')
# os.chdir('pictures')
# os.mkdir('thumbnails')
# os.chdir('thumbnails')
# os.mkdir('tmp')
# os.chdir('../')
 
print(os.getcwd())

from time import time

start = time()
c=0
for x in range(8000):
    for y in range(8000):
        if x > y:
            c += 1
print(c, time()- start)

start1 = time()
c=0
for x in range(8000):
    for y in range(8000,0,-1):
        if x > y:
            c += 1
print(c, time()- start1)

start = time()
c=0
for x in range(8000):
    for y in range(8000):
        if x > y:
            c += 1
print(c, time()- start)

start1 = time()
c=0
for x in range(8000):
    for y in range(8000,0,-1):
        if x > y:
            c += 1
print(c, time()- start1)

start = time()
c=0
for x in range(8000):
    for y in range(8000):
        if x > y:
            c += 1
print(c, time()- start)

start1 = time()
c=0
for x in range(8000):
    for y in range(8000,0,-1):
        if x > y:
            c += 1
print(c, time()- start1)