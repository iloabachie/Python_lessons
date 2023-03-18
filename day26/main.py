name = 'udemezue'
caps = [l.upper() for l in name]
print(caps)

lisst = list(name)
print(lisst)

double = [num*2 for num in range(5)]
print(double)

with open('D:/documents/Python lessons/AngelaYu\day26/file1.txt') as file1:
    # print(file1)
    file1 = list(file1)
    # or use below to make list
    # data1 = file1.readlines()
    # print(file1)

with open('D:/documents/Python lessons/AngelaYu\day26/file2.txt') as file2:
    # print(file2)
    file2 = list(file2)
    # print(file2)

# file1 = [digit.strip() for digit in file1]
# file2 = [digit.strip() for digit in file2]
# print(file1)
# print(file2)


file3 = [digit.strip() for digit in file2 if digit in file1]
# also works
# file3 = [int(digit) for digit in file2 if digit in file1] 
print(file3)


# dictionary comprehension
import random

students = ['ade', 'sesan', 'tolu', 'olu', 'bolu', 'tope']

new_dict = {name:random.randint(30, 100) for name in students}
print(new_dict)

passed_students = {name:new_dict[name] for name in new_dict if new_dict[name] > 50}
print(passed_students)

passed_students = {student:score for (student, score) in new_dict.items() if score > 50}
print(passed_students)
print(new_dict.items())

for (name) in new_dict.items():
    print(name)