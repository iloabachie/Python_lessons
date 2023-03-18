s = "babad"
# s = 'Corporate representative for Alex Jones company makes admission on the stand'

palindromes = []

for l in range(len(s)):
    for f in range(len(s)):
        if l > f:
            q = s[f:l]
            r = q[::-1]

            if q == r:
                palindromes.append(q)

length = [len(item) for item in palindromes] # list comprehension

max = max(length)

longest = []
for _ in palindromes:
    if len(_) == max:
        longest.append(_)
print(length)
print(palindromes)
print(longest)
longest.clear()
print(longest)

# with open('linux.txt') as file:
#     contents = file.read()
#     print(contents)



newlist = [x for x in range(9999) if x % 6 == 0] # list comprehension.

print(newlist)