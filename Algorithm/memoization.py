from timeit import timeit
# Recursive without memoization
def fibonacci(n):
    if n in [1, 2]: return 1
    return fibonacci(n-1) + fibonacci(n-2)

# for n in range(1,100):
#     print(n, fibonacci(n))
    

# Recursive with memoization
memoize = {}
def fibonacci_m(n=100):    
    if n in memoize:
        return memoize[n]
    if n in [1, 2]: return 1
    if n not in memoize:
        memoize[n] = fibonacci_m(n-1) + fibonacci_m(n-2)
    return memoize[n]
    
for n in range(1,100):
    print(n, fibonacci_m(n))
    
import functools

print(dir(functools))

# using the LRU module for memoization
@functools.lru_cache(maxsize=1000)
def fibonacci_lru(n=100):
    if n in [1, 2]: return 1
    return fibonacci_lru(n-1) + fibonacci_lru(n-2)

for n in range(1,100):
    print(n, fibonacci_lru(n))
    

def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)

for n in range(1,100):
    print(n, factorial(n))


print(timeit(stmt=fibonacci_m, number=1000000))
print(timeit(stmt=fibonacci_lru, number=1000000))
print(memoize)

for n in range(1,100):
    print(fibonacci_lru(n + 1) / fibonacci_lru(n))

