set1 = {1, 2, 3, 4, 5, 6}
set2 = {5, 6, 7, 8, 9, 10, 11}

set1.add(7)
print(set1, set2)
set3 = set1.difference(set2)
print(set3)
set1.difference_update(set2)
print(set1, set2)
set1.discard(1)  # removes element but raises no error if not found
print(set1, set2)
set5 = set1.intersection(set2)   # Returns a set, that is the intersection of two or more sets
print(set5)
set1.intersection_update(set2)   # Removes the items in this set that are not present in other, specified set(s)
print(set1.isdisjoint(set2))
set3.pop() # removes random element
print(set3)
set3.remove(3)   # removes specified element or raise error if not found
print(set3)

sy_diff = set1.symmetric_difference(set2)	# Returns a set with the symmetric differences of two sets

set1.symmetric_difference_update(set2)  #inserts the symmetric differences from this set and another

union = set1.union(set2)	# Return a set containing the union of sets
set1.update(set2)  #	Update the set with another set, or any other iterable