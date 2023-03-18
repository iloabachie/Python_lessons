"""An unsolved mathematical problem.  Is it true that for all numbers it ends in 1?"""

from operator import itemgetter
from collections import Counter
import sys

y = [19**120]
y = [*range(1, 1000001)]
listOfNumCountMax = []

for z in y:
    values_of_x = []
    count = 0
    x = z
    while x != 1:
        if x % 2 == 0:
            x /= 2
        else:
            x = x * 3 + 1
        values_of_x.append(int(x))
        count += 1
    if values_of_x != []:
        listOfNumCountMax.append([z, count, max(values_of_x)])
        
sys.stdout = open('3xplus2.txt', 'a')

print("\nList of lists showing the number, number of steps, max value")
print(listOfNumCountMax)
print("\n\nList of counts")
print([*map(itemgetter(1), listOfNumCountMax)])
print("\n\nList of maximums")
print([*map(itemgetter(2), listOfNumCountMax)])
print("\n\nSorted by count of steps")
print(sorted([*map(itemgetter(1), listOfNumCountMax)]))
print("\n\nSorted by Max value")
print(sorted([*map(itemgetter(2), listOfNumCountMax)]))
print("\n\nCounts teh number of times the number of steps occurs")
print(Counter(map(itemgetter(1), listOfNumCountMax)))
print("\n\nCounts the number of times the max value occurs")
print(Counter(map(itemgetter(2), listOfNumCountMax)))

sys.stdout.close()
sys.stdout = sys.__stdout__
print("Output saved to file")


steps = set([*map(itemgetter(2), listOfNumCountMax)])
minimum = min(steps)
maximum = max(steps)

unused_count = []
for _ in range(minimum, maximum + 1):
    if _ not in steps:
        unused_count.append(_)


with open('unused.txt', 'a') as sys.stdout:
    print(unused_count)

sys.stdout = sys.__stdout__
print("Output saved to file")