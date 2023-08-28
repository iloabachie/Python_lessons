import threading
from timeit import timeit

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:

        def contains_duplicate(array):
            nums = tuple(enumerate(array))
            return bool([(i, j) for i, a in nums for j, b in nums if abs(a - b) <= valueDiff and i != j and abs(i - j) <= indexDiff])

        def split_list(array):
            size = len(array) // 1000
            lists = []
            while array:
                lists.append(array[:size])
                array = array[size:]
            return lists    

        smaller_lists = split_list(nums)
        threads = []
        results = []
        for sub in smaller_lists:
            thread = threading.Thread(target=lambda: results.append(contains_duplicate(sub)))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        return any(results)  


class Solution1:
    def containsNearbyAlmostDuplicate(self) -> bool:
        def contains_duplicate(array):
            nums = tuple(enumerate(array))
            return bool([(i, j) for i, a in nums for j, b in nums if abs(a - b) <= valueDiff and i != j and abs(i - j) <= indexDiff])

        def split_list(array):
            size = len(array) // 200
            lists = []
            while array:
                lists.append(array[:size])
                array = array[size:]
            return lists    

        smaller_lists = split_list(nums)
        threads = []
        results = []
        for sub in smaller_lists:
            thread = threading.Thread(target=lambda: results.append(contains_duplicate(sub)))
            threads.append(thread)
            thread.start()
            
        for thread in threads:
            thread.join()
        return any(results)

        
class Solution2:
    def containsNearbyAlmostDuplicate(self) -> bool:
        def contains_duplicate(array):
            nums = tuple(enumerate(array))
            return bool([(i, j) for i, a in nums for j, b in nums if abs(a - b) <= valueDiff and i != j and abs(i - j) <= indexDiff])

        def split_list(array):
            size = len(array) // 1000
            lists = []
            while array:
                lists.append(array[:size])
                array = array[size:]
            return lists    

        smaller_lists = split_list(nums)
        threads = []
        results = []
        for sub in smaller_lists:
            thread = threading.Thread(target=lambda: results.append(contains_duplicate(sub)))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        return any(results)


   
nums = [*range(150)]
valueDiff = 16
indexDiff = 35

print(dir(threading))
# print(timeit(stmt=Solution1().containsNearbyAlmostDuplicate, number= 3))
# print(timeit(stmt=Solution2().containsNearbyAlmostDuplicate, number= 3))


h = [1,2,3]

def stcopy():
    y = h[:]
def stcopy1():
    y = h.copy()

print(timeit(stmt=stcopy))
print(timeit(stmt=stcopy1))