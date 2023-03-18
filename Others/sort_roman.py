nums = [1, 1, 1,2,3,4,5,3,4,5,1,2]

num_new = []

num_set = set(nums)
print(nums, num_set)

for i in num_set:
    for j in nums:
        if i == j:
            num_new.append(i)

print(num_new)


# -------------------------------------------
from random import randint

arab = randint(0, 3999)
arabic = str(arab)

if len(arabic) == 3:
    arabic = '0' + arabic
elif len(arabic) == 2:
    arabic = '00' + arabic
elif len(arabic) == 1:
    arabic = '000' + arabic

arabic = list(arabic)

numeral = []

x = int(arabic[0])
if x == 1 or x == 2 or x == 3:
    y = x * 'M'
    numeral.append(y)

x = int(arabic[1])
if x == 1 or x ==2 or x == 3:
    y = x * 'C'
    numeral.append(y)
elif x == 4:
    y = 'CD'
    numeral.append(y)
elif x == 5:
    y = 'D'
    numeral.append(y)
elif x == 6 or x == 7 or x == 8:
    y = 'D' + ((x-5)* 'C')
    numeral.append(y)
elif x == 9:
    y = 'CM'
    numeral.append(y)

x = int(arabic[2])
if x == 1 or x ==2 or x == 3:
    y = x * 'X'
    numeral.append(y)
elif x == 4:
    y = 'XL'
    numeral.append(y)
elif x == 5:
    y = 'L'
    numeral.append(y)
elif x == 6 or x == 7 or x == 8:
    y = 'L' + ((x-5)* 'X')
    numeral.append(y)
elif x == 9:
    y = 'XC'
    numeral.append(y)

x = int(arabic[3])
if x == 1 or x ==2 or x == 3:
    y = x * 'I'
    numeral.append(y)
elif x == 4:
    y = 'IV'
    numeral.append(y)
elif x == 5:
    y = 'V'
    numeral.append(y)
elif x == 6 or x == 7 or x == 8:
    y = 'V' + ((x-5)* 'I')
    numeral.append(y)
elif x == 9:
    y = 'IX'
    numeral.append(y)

answer = ''.join(numeral)

print(f'{str(arab)} is {answer}')

# ----------------------------------------


# numeral = input('Enter the roman numeral:\n>> ').upper()
numeral = answer

ROMAN = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
VALUE = [1, 5, 10, 50, 100, 500, 1000]

num_array = []
arabic = 0


for i in numeral:
    for j in ROMAN:
        if i == j:
            v = VALUE[ROMAN.index(i)]
            num_array.append(v)

for i in range(len(num_array)):
    if i + 1 == len(num_array) and num_array[i-1] >= num_array[i]:
        arabic += num_array[i]
    elif i + 1 == len(num_array) and num_array[i-1] < num_array[i]:
        pass
    elif i - 1 < 0 and num_array[i] < num_array[i + 1]:
        arabic += (num_array[i + 1] - num_array[i])
    elif i - 1 < 0 and num_array[i] >= num_array[i + 1]:
        arabic += num_array[i]
    elif num_array[i] < num_array[i + 1]:
        arabic += (num_array[i + 1] - num_array[i])
    elif num_array[i] > num_array[i - 1]:
        pass
    elif num_array[i] >= num_array[i + 1]:
        arabic += num_array[i]

print(f'{numeral} is {arabic}')