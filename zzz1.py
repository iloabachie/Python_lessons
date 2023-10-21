import itertools


class Solution:
    def subsets(self, s: list[int]) -> list[list[int]]:
        return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))



print(*Solution().subsets('abcdef'), sep='\n')


print(*itertools.chain.from_iterable('hello'))



import string

letters = string.ascii_uppercase
numbers = '0123456789'

print(*[[l + n for n in numbers] for l in letters], sep='\n')


print([l + n for l in letters for n in numbers])

def repeat(num):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(num=3)
def greet(name):
    print(f"Hello, {name}!")

greet("John")



import getpass

def get_masked_password(prompt="Enter your password: "):
    return getpass.getpass(prompt)

if __name__ == "__main__":
    password = get_masked_password()
    print(f"You entered: {password}")
