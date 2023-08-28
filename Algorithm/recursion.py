nums = [2,3,6,7,8,1,9]
class Solution:
    def find132pattern(self, nums: list[int]) -> bool:     
        nums = [value for index, value in enumerate(nums[:-1]) if nums[index] != nums[index + 1]] + [nums[-1]]
        print(len(nums))
        while True: 
            if len(nums) < 3 or len(set(nums)) < 3:
                return False 
            if max(nums) == nums[0]:
                nums.pop(0)
                continue
            if max(nums) == nums[-1] or min(nums) == nums[-1]:
                nums.pop()
                continue
            max_index = nums.index(max(nums))
            
            if min(nums[0:max_index]) < max([x for x in nums[max_index + 1:] if x != max(nums)]):
                return True
            nums.pop(max_index)
        return False

# print(Solution().find132pattern(nums))

# import timeit

# my_list = list(range(30009))

# # Measure time for popping the last item
# pop_time = timeit.timeit(lambda: my_list.pop(), number=20000)


# my_list = list(range(30009))
# # Measure time for using a slice to exclude the last item
# slice_time = timeit.timeit(lambda: my_list[:-1], number=20000)

# print("Time for popping the last item:", pop_time)
# print("Time for using a slice to exclude the last item:", slice_time)


class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        print(nums)
        stack = []
        s3largest = float('-inf')
        
        for i in range(len(nums)-1, -1, -1):
            print(f'{nums[i]=}   {s3largest=}')
            if nums[i] < s3largest:
                return True
            while stack and stack[-1] < nums[i]:
                s3largest = stack.pop()
                print(f'{s3largest}')
            stack.append(nums[i])
            print(f'{stack=}', "contains nums[i]")
            print("+++++++++++++++++++++++")
        
        return False
    
nums=[*range(10, -1, -1)]
# print(Solution().find132pattern(nums))


import timeit
import copy

a = [*range(1000)]

def one():
    reversed([*range(1000)])    

def two():
    [*range(1000)][::-1]

def tre():
    [*range(1000)].reverse()

# print(sum(timeit.repeat(stmt=one, repeat=10, number=100000))/10)
# print(sum(timeit.repeat(stmt=two, repeat=10, number=100000))/10)
# print(sum(timeit.repeat(stmt=tre, repeat=10, number=100000))/10)

a=[1,2,3,4,5]

a.reverse()
print(a)

x = 10


def testing(x,y):   
    print(y)
    def inner():
        nonlocal y
        y = 23
        def innerinner():
            print(x, '|', y)
            
        innerinner()
    print(y)
    inner()
    print(y)
        
testing(16,18)


def check():
    global zz
    (zz:=16)
    print(zz)

# print(zz)
check()
print(zz)

