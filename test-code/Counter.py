from random import randint
from collections import Counter

nums = []
for n in range(10):
    nums.append(randint(0,40))

# nums = [10, 3, 10, 2, 5, 4, 8, 7, 5, 4, 6, 8, 8, 5, 2]
print('unordered = ', nums)

def sorts(unord):
    def sor(unord):    
        for i in range(len(unord)):
            if i + 1 < len(unord):
                p = unord[i]
                q = unord[i + 1]
                if p > q:
                    unord[i], unord[i + 1] = q, p
        return unord                 
    for i in range (len(unord)):
        sor(unord)
     
    return unord

ordered = sorts(nums)
print('ordered = ', ordered)


print(111111111111111, Counter(ordered))
print(222222222222222222, Counter(nums))
print(3333333333333333333333, Counter(ordered) - Counter(nums))
print("_________")



print(globals())
print()