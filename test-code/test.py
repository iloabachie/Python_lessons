# n = int(input('Type a number, and its factorial will be printed: '))

# if n < 0:
#     raise ValueError('You must enter a non-negative integer')

# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i

#     print(factorial)


lists = [1, 3, 2, 4, 1, 2, 3, 4, 5]
lists = list(set(lists))
print('1', lists)

dicttionary = dict.fromkeys(lists)
print('2', dicttionary)
new_list = list(dicttionary)
print('3', new_list)

print('-----------------------')



# # -------------------------------------
class Animal:
    def __init__(self):
        self.eyes = 2
        self.legs = 4
        self.tail = True
    
    def move(self):
        print('this animal moves')
    
    def feel(self):
        print('this animal feels')


class Dog1(Animal):
    def __init__(self):
        super().__init__()
        self.skin = 'hairy'

    def speak(self):
        print('bark bark')
    
    def move1(self):
        super().move()
        print('runs on 4 legs')

suzy = Dog1()

print(suzy.skin)
print(suzy.eyes)

suzy.move1()
suzy.feel()
suzy.speak()


# # ------------------------------------
# class Dog:
#     def __init__(self):
#         self.temperament = "loyal"
 
# class Labrador(Dog):
#     def __init__(self):
#         super().__init__()
#         self.temperament = "gentle"

# doggo = Dog()
# print(f"A dog is {doggo.temperament}")
 
# sparky = Labrador()
# print(f"Sparky is {sparky.temperament}")




# from collections import Counter


# a = 'dsfksdkfasdow409wetoidfgpo3487t934759843598y4uh54h'

# my_counter = Counter(a)

# print(my_counter)

# import timeit
# print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))

# print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))

# print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))

# one = "#".join(str(n) for n in range(5))

# two = "$".join([str(n) for n in range(5)])

# three = "-".join(map(str, range(5)))

# print(one, two, three)

# check = map(str, range(6))
# print(check)
# print(list(check))

# check = map(str, range(6))
# print(check)
# print(list(check))

# import time
# import random

# for _ in range(15):
#     print("every 5 seconds something shoulld appear")
#     # time.sleep(1)
#     print(random.randint(-270, 270))



#find the longest palindrome in the word.

# with open('high_score.txt') as file:
#     high_score = file.read()
# print(high_score)

# with open('high_score.txt', mode='a') as file:
#     file.write(f'{high_score}')



# hi = [2,4,5,6,7,8,9,0,0,8,7,6]
# double = []
# for _ in hi:
#     double.append(_*2)

# print(2, double)
# triple = []
# for n in hi:
#     triple.append(n*3)

# print(3, triple)

# import random

# print(random.random())


seasons = ['Spring', 'Summer', 'Fall', 'Winter']
def enumerat(sequence, start=0):
    n = 0
    for elem in sequence:
        yield n, elem
        n += 1
    
for i, j in enumerate(seasons):
    print(i, j)
# dict comprehension

weather_c = {
    'Monday': 22,
    'Tuesday': 33,
    'Wednesday': 25,
    'Thursday': 14,
    'Friday': 23,
    'Saturday': 7
}

weather_f = {item: (c * 5 / 9 + 32) for item, c in weather_c.items() if c % 2 == 0}

print(weather_f)

print("****", weather_c.items())



def permute(string, pocket=''):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket)
            
permute('ABC', '')

import pdb
from tkinter import Y
print(dir(pdb))

import collections

print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print(collections.Counter({'a':2, 'b':3, 'c':1}))
print(collections.Counter(a=2, b=3, c=1))

c = collections.Counter('abcdaab')

for letter in 'abcde':
    print(f'{letter} : {c[letter]}')

c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabetaa')

print('C1:', c1)
print('C2:', c2)

print('\nCombined counts:')
print(c1 + c2)

print('\nSubtraction:')
print(c1 - c2)

print('\nIntersection (taking positive minimums):')
print(c1 & c2)

print('\nUnion (taking maximums):')
print(c1 | c2)







def square(nums: list):
    for _ in nums:
        x = _**2
        yield x



sq = square([1, 2, 3, 4, 5])

# print(list(sq))
# print(next(sq), next(sq), next(sq), next(sq), next(sq))
# # print(next(sq))
# # print(next(sq))
# # print(next(sq))
# # print(next(sq))


print(next(sq) + next(sq))

def pop(list):
    def get_last(my_list):
        return my_list[len(my_list)-1]
    list.remove(get_last(list))
    return list

a = [1,2,3,4,5,6]
a.remove(4)
print(pop(a))
print(pop(a))
print(pop(a))


def nth_power(exponent):
    def powerof(num):
        return pow(num, exponent)
    return powerof


cube = nth_power(3)(999)

print(cube)

squ = nth_power(2)

print(squ(16))


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

 


print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

for x in "00123dfgh65478900":
    try:
        print(int(x))
    except ValueError:
        print(x)
        
def add(*args):
    y = 0
    for n in args:
        y += n
    return y

z = add(5,6,9,7,3,40,25)

print(z)


def calculate(n, **kwargs):
    n *= float(kwargs.get('x'))
    n += float(kwargs.get('pl'))
    print(n)
    
calculate(3, pl=3, x=6)


i = 3
while i > 0:
    i -= 2
    print('*')
    if i == 2:
        break
else:
 
    print('*mmm')
    
try:
    print('try' + "try")
except NameError as error:
    print('except')
    print(error)
    
else:
    print('else')
finally:
    print('finally')

print(''.join(sorted('32sdfgsdfg1')))

tem  = list('321')
tem.sort()

print(tem)

try:
    print(5/0)

except (ValueError, ZeroDivisionError):
    print("Too bad...")
except SyntaxError:
    print("Sorry, something went wrong...")
    
    
    
d = {}
d[1] = 1
d['hi'] = 2
d[1] += 1

print(d)
 
sum = 0
 
for k in d:
    print(k)
    sum += d[k]
 
print(sum)

# num = 1
 
 
def func():
    # num = 1
    # global num
    num = 1
    num = num + 3
    print(num)
 
 
func()
 
class Cat:
    Species = 1
 
    def get_species(self):
        return 'kitty'
 
 
class Tiger(Cat):
    def get_species(self):
        return 'tiggy'
 
    def set_species(self):
        pass
 
 
creature = Tiger()
print(hasattr(creature, "Species"),
      hasattr(Cat, "set_species"))


# check in thonny
# x = [0, 1, 2]
# x.insert(0, 1)
# print(x)
# del x[1]
# print(x)
# print(sum(x))

x = True
y = False
z = False
 
if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)


x = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
 
def func(data):
    res = data[0][0]
    for da in data:
        for d in da:
            if res < d:
                res = d
    return res
 
print(func(x[0]))

print(len([i for i in range(-1, -2)]))

import math
 
result = math.e != math.pow(2, 4)
print(int(result))


list1 = [1, 3]
list2 = list1
list1[0] = 4
print(list2)

def func(x):
    return 1 if x % 2 != 0 else 2
 
 
print(func(func(1)))

active_list = [123, 456, 789, 159]

code = 123

{code} if {len(code) == 4} else f'0{code}'

print(f'{code} unblocked' if code in active_list else f'{code} blocked')



print(1 if 1==1 else 0.5 if 2>1 else 1)




import random

print(type(print(type(type(type('hello'))))))

print('hello'.__class__)

print(random.random() - random.random())

print(0**0)

t = '%(a)s %(b)s %(c)s'
print(t % dict(a='Welcome', b='to', c='Turing'))

class Developer:
    def __init__(self):
        self.__seniority = 'Junior'
        self.skills = '88'

    def display(self):

        print('Welcome to Turing with {seniority} developer with skill {skills}'.format(seniority=self.__seniority, skills=self.skills))

class NodeJS(Developer):
    def __init__(self):
        super().__init__() 
        self.__seniority = 'Senior'
        self.skills = 'NodeJS'

c = NodeJS() 
c.display()


print(c)
# print(c._Developer__seniority)
# print(c.skills)

import re
result = re.findall("Welcome to Turing", 'Welcome;, 1')
print(result)



# -------------------------------------------------
# how to time a function using decorators

def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        __ = func(*args, **kwargs)
        total = time.time() - start
        print('Total runtime: ', total)
        return __
    return wrapper

# @timer
def forloop():
    y = [x for x in range(99999999) if x % 57559 == 3 and x % 48596 == 16]
    print('Comprehension', y)
    return y
        
@timer
def forloop2():
    x = []
    for y in range(99999999):
         if y % 57559 == 3 and y % 48596 == 16:
             x.append(y)
    print('For loop', x)
    return x

# forloop()
# pppp = forloop2()

# forloop = timer(forloop)

# forloop()    

# print('[[[', pppp)
# -------------------------------------------------------


phrase = 'PAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRINGPAYPAIRINGPAYPALISHIRINGPAYPALISHIRIN'

@timer
def zigzag(word: str, row: int) -> str:
    index = [_ for _ in range(row)]
    index = index + index[-2:0:-1] 
    index = index * (len(word) // len(index) + 1)
    word_list = list(word)
    together = list(zip(index, word_list))
    new_string = []
    
    for _ in range(len(together)):
        new_string += [y for x, y in together if x == _]
        
    print('zigzag:', ''.join(new_string) if len(''.join(new_string)) < 20 else 'time test')
    
       
zigzag(phrase, 5)  

@timer
def zigzags(word: str, row: int) -> str:
    index = [_ for _ in range(row)]
    index = index + (index[::-1])[1:-1]
    index = index * (len(word) // len(index) + 1)
    word_list = list(word)
    together = list(zip(index, word_list))
    new_string = []
    
    for _ in range(len(together)):
        new_string += [y for x, y in together if x == _]
        
    print('zigzags:', ''.join(new_string) if len(''.join(new_string)) < 20 else 'time test')


# zigzag(phrase, 5)     
# zigzags(phrase, 5)  
# zigzag(phrase, 5)     
# zigzags(phrase, 5)  
# zigzag(phrase, 5)     
# zigzags(phrase, 5)  
# zigzag(phrase, 5)     
# zigzags(phrase, 5)  


data = ['a', 'b', 'c', 'd']

import copy
newlist = data.copy()


print(newlist)

print(id(newlist), id(data))

print(vars(copy))


MCC_LIST = [742, 763, 780, 1520, 1711, 1731, 1740, 1750, 1761, 1771, 1799, 2732, 2741, 2791, 2842, 3000, 3001, 3002, 3003, 3004, 3005, 3006, 3007, 3008, 3009, 3010, 3011, 3012, 3013, 3014, 3015, 3016, 3017, 3018, 3019, 3020, 3021, 3022, 3023, 3024, 3025, 3026, 3027, 3028, 3029, 3030, 3031, 3032, 3033, 3034, 3035, 3036, 3037, 3038, 3039, 3040, 3041, 3042, 3043, 3044, 3045, 3046, 3047, 3048, 3049, 3050, 3051, 3052, 3053, 3054, 3055, 3056, 3057, 3058, 3059, 3060, 3061, 3062, 3063, 3064, 3065, 3066, 3067, 3068, 3069, 3070, 3071, 3072, 3073, 3075, 3076, 3077, 3078, 3079, 3081, 3082, 3083, 3084, 3085, 3086, 3087, 3088, 3089, 3090, 3094, 3096, 3097, 3098, 3099, 3100, 3102, 3103, 3105, 3106, 3110, 3111, 3112, 3115, 3117, 3118, 3125, 3126, 3127, 3129, 3130, 3131, 3132, 3133, 3135, 3136, 3137, 3138, 3141, 3143, 3144, 3145, 3146, 3148, 3151, 3154, 3156, 3159, 3161, 3164, 3165, 3167, 3170, 3171, 3172, 3174, 3175, 3176, 3177, 3178, 3180, 3181, 3182, 3183, 3184, 3185, 3186, 3187, 3188, 3190, 3191, 3192, 3193, 3195, 3196, 3197, 3198, 3199, 3200, 3203, 3204, 3206, 3207, 3211, 3212, 3213, 3215, 3216, 3217, 3218, 3219, 3220, 3221, 3222, 3223, 3226, 3228, 3229, 3231, 3233, 3234, 3235, 3236, 3238, 3239, 3240, 3241, 3242, 3243, 3245, 3246, 3247, 3248, 3251, 3252, 3253, 3254, 3256, 3259, 3260, 3261, 3262, 3263, 3266, 3267, 3268, 3275, 3276, 3277, 3279, 3280, 3282, 3284, 3285, 3286, 3287, 3291, 3292, 3293, 3294, 3295, 3296, 3297, 3298, 3299, 3300, 3301, 3303, 3308, 3351, 3352, 3353, 3354, 3355, 3357, 3359, 3360, 3361, 3362, 3364, 3366, 3368, 3370, 3374, 3376, 3380, 3381, 3385, 3386, 3387, 3388, 3389, 3390, 3391, 3393, 3394, 3395, 3396, 3398, 3400, 3405, 3409, 3412, 3414, 3420, 3421, 3423, 3425, 3427, 3428, 3429, 3430, 3431, 3432, 3433, 3434, 3435, 3436, 3437, 3438, 3439, 3441, 3501, 3502, 3503, 3504, 3505, 3506, 3507, 3508, 3509, 3510, 3511, 3512, 3513, 3514, 3515, 3516, 3517, 3518, 3519, 3520, 3521, 3522, 3523, 3524, 3525, 3526, 3527, 3528, 3529, 3530, 3531, 3532, 3533, 3534, 3535, 3536, 3537, 3538, 3539, 3540, 3541, 3542, 3543, 3544, 3545, 3546, 3547, 3548, 3549, 3550, 3551, 3552, 3553, 3554, 3555, 3556, 3557, 3558, 3559, 3560, 3561, 3562, 3563, 3564, 3565, 3566, 3567, 3568, 3569, 3570, 3571, 3572, 3573, 3574, 3575, 3576, 3577, 3578, 3579, 3580, 3581, 3582, 3583, 3584, 3585, 3586, 3587, 3588, 3589, 3590, 3591, 3592, 3593, 3594, 3595, 3596, 3597, 3598, 3599, 3600, 3601, 3602, 3603, 3604, 3605, 3606, 3607, 3608, 3609, 3610, 3611, 3612, 3613, 3614, 3615, 3616, 3617, 3618, 3619, 3620, 3621, 3622, 3623, 3624, 3625, 3626, 3627, 3628, 3629, 3630, 3631, 3632, 3633, 3634, 3635, 3636, 3637, 3638, 3639, 3640, 3641, 3642, 3643, 3644, 3645, 3646, 3647, 3648, 3649, 3650, 3651, 3652, 3653, 3654, 3655, 3656, 3657, 3658, 3659, 3660, 3661, 3662, 3663, 3664, 3665, 3666, 3667, 3668, 3669, 3670, 3671, 3672, 3673, 3674, 3675, 3676, 3677, 3678, 3679, 3680, 3681, 3682, 3683, 3684, 3685, 3686, 3687, 3688, 3689, 3690, 3691, 3692, 3693, 3694, 3695, 3696, 3697, 3698, 3699, 3700, 3701, 3702, 3703, 3704, 3705, 3706, 3707, 3708, 3709, 3710, 3711, 3712, 3713, 3714, 3715, 3716, 3717, 3718, 3719, 3720, 3721, 3722, 3723, 3724, 3725, 3726, 3727, 3728, 3729, 3730, 3731, 3732, 3733, 3734, 3735, 3736, 3737, 3738, 3739, 3740, 3741, 3742, 3743, 3744, 3745, 3746, 3747, 3748, 3749, 3750, 3751, 3752, 3753, 3754, 3755, 3756, 3757, 3758, 3759, 3760, 3761, 3762, 3763, 3764, 3765, 3766, 3767, 3768, 3769, 3770, 3771, 3772, 3773, 3774, 3775, 3776, 3777, 3778, 3779, 3780, 3781, 3782, 3783, 3784, 3785, 3786, 3787, 3788, 3789, 3790, 3791, 3792, 3793, 3794, 3795, 3796, 3797, 3798, 3799, 3800, 3801, 3802, 3803, 3804, 3805, 3806, 3807, 3808, 3809, 3810, 3811, 3812, 3813, 3814, 3815, 3816, 3817, 3818, 3819, 3820, 3821, 3822, 3823, 3824, 3825, 3826, 3827, 3828, 3829, 3830, 3831, 3832, 3833, 3834, 3835, 3836, 3837, 3838, 3998, 4011, 4111, 4112, 4119, 4121, 4131, 4214, 4215, 4225, 4411, 4457, 4468, 4511, 4582, 4722, 4723, 4761, 4784, 4785, 4789, 4812, 4813, 4814, 4815, 4816, 4821, 4829, 4899, 4900, 5013, 5021, 5039, 5044, 5045, 5046, 5047, 5051, 5065, 5072, 5074, 5085, 5094, 5099, 5111, 5122, 5131, 5137, 5139, 5169, 5172, 5192, 5193, 5198, 5199, 5200, 5211, 5231, 5251, 5261, 5262, 5271, 5300, 5309, 5310, 5311, 5331, 5399, 5411, 5422, 5441, 5451, 5462, 5499, 5511, 5521, 5531, 5532, 5533, 5541, 5542, 5551, 5552, 5561, 5571, 5592, 5598, 5599, 5611, 5621, 5631, 5641, 5651, 5655, 5661, 5681, 5691, 5697, 5698, 5699, 5712, 5713, 5714, 5715, 5718, 5719, 5722, 5732, 5733, 5734, 5735, 5811, 5812, 5813, 5814, 5815, 5816, 5817, 5818, 5912, 5921, 5931, 5932, 5933, 5935, 5937, 5940, 5941, 5942, 5943, 5944, 5945, 5946, 5947, 5948, 5949, 5950, 5960, 5961, 5962, 5963, 5964, 5965, 5966, 5967, 5968, 5969, 5970, 5971, 5972, 5973, 5975, 5976, 5977, 5978, 5983, 5992, 5993, 5994, 5995, 5996, 5997, 5998, 5999, 6010, 6011, 6012, 6050, 6051, 6051, 6211, 6300, 6381, 6399, 6513, 6529, 6530, 6531, 6532, 6533, 6534, 6535, 6536, 6537, 6538, 6540, 6555, 7011, 7012, 7013, 7032, 7033, 7210, 7211, 7216, 7217, 7221, 7230, 7251, 7261, 7273, 7276, 7277, 7278, 7296, 7297, 7298, 7299, 7311, 7321, 7322, 7332, 7333, 7338, 7339, 7342, 7349, 7361, 7372, 7375, 7379, 7392, 7393, 7394, 7395, 7399, 7511, 7512, 7513, 7519, 7523, 7524, 7531, 7534, 7535, 7538, 7539, 7542, 7549, 7622, 7623, 7629, 7631, 7641, 7692, 7699, 7778, 7800, 7801, 7802, 7829, 7832, 7841, 7911, 7922, 7929, 7932, 7933, 7941, 7990, 7991, 7992, 7993, 7994, 7995, 7996, 7997, 7998, 7999, 8011, 8021, 8031, 8041, 8042, 8043, 8044, 8049, 8050, 8062, 8071, 8099, 8111, 8211, 8220, 8241, 8244, 8249, 8299, 8351, 8398, 8641, 8651, 8661, 8675, 8699, 8734, 8911, 8931, 8999, 9211, 9222, 9223, 9311, 9399, 9401, 9402, 9405, 9406, 9700, 9701, 9702, 9751, 9752, 9753, 9754, 9950]