from regex import imported 
print(len(imported))


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


print(Solution().containsNearbyAlmostDuplicate(imported, 350, 100))
print(timeit(stmt=Solution().containsNearbyAlmostDuplicate(imported, 35000, 100), number= 3))        
nums = imported[:500]
valueDiff = 100
indexDiff = 35000


print(timeit(stmt=Solution1().containsNearbyAlmostDuplicate, number= 300))
print(timeit(stmt=Solution2().containsNearbyAlmostDuplicate, number= 300))