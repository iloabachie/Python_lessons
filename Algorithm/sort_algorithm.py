from timeit import timeit
from copy import deepcopy
from time import time


def timerfn(funct):
    def wrapper(*args):
        def _():
            funct(*args)
        time = timeit(stmt=_, number=1000)
        print(f'{funct.__name__} took {time} seconds')
    return wrapper

@timerfn
def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j+ 1], array[j]
    return array

@timerfn
def selection_sort(array):
    for i in range(len(array)-1):
        min_index=i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index=j 
        if i != min_index: 
            array[i], array[min_index] = array[min_index], array[i]
    return array   

@timerfn
def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while temp < array[j] and j > -1:
            array[j+1] = array[j]
            array[j] = temp
            j -= 1
    return array

# @timerfn
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = []
        right = []
        for i in array[1:]:
            if i < pivot:
                left.append(i)
            else:
                right.append(i)
    return quick_sort(left) + [pivot] + quick_sort(right)

@timerfn
def builtin_sort(array):
    return sorted(array)

array=[2,3,9,7,4,5,6,0,3,5,7,2,8,3,3]*100

# array = [*range(991,0,-1)]

a = time()
# bubble_sort(deepcopy(array))
print(time() - a)

a = time()
# selection_sort(deepcopy(array))
print(time() - a)

a = time()
insertion_sort(deepcopy(array))
print(time() - a)

a = time()
quick_sort(deepcopy(array))
print(time() - a)

a = time()
builtin_sort(deepcopy(array))
print('builtin', time() - a)

import collections, math
def countAnagrams(s: str) -> int:
    ans = math.prod([math.factorial(len(t))//math.prod([math.factorial(num) for num in collections.Counter(t).values()]) for t in s.split()])
    return ans % (10**9 + 7)