import itertools


class Solution:
    def subsets(self, s: list[int]) -> list[list[int]]:
        return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))



print(*Solution().subsets('abcdef'), sep='\n')


print(*itertools.chain.from_iterable('hello'))



import string

letters = string.ascii_uppercase
numbers = '0123456789'

print(*[[l + n for n in numbers] for l in letters], sep='\n')


print([l + n for l in letters for n in numbers])

def repeat(num):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(num=3)
def greet(name):
    print(f"Hello, {name}!")

greet("John")



# import getpass

# def get_masked_password(prompt="Enter your password: "):
#     return getpass.getpass(prompt)

# if __name__ == "__main__":
#     password = get_masked_password()
#     print(f"You entered: {password}")


def hi(param: int):
    return param

print(hi('hello'))


my_dict = dict()

print(my_dict.get('name'))
print(my_dict.setdefault('hi', 'man'))
print(my_dict)


random_words = [
    "Apple", "Banana", "Cat", "Dog", "Elephant", "Fish", "Grape", "Hat", "Igloo", "Jelly",
    "Kangaroo", "Lemon", "Monkey", "Noodle", "Orange", "Penguin", "Quilt", "Rabbit", "Strawberry", "Tiger",
    "Umbrella", "Volcano", "Watermelon", "Xylophone", "Yak", "Zebra", "Airplane", "Balloon", "Carrot", "Dolphin",
    "Eggplant", "Flamingo", "Giraffe", "Hamburger", "Ice cream", "Jigsaw", "Koala", "Lighthouse", "Mushroom", "Narwhal",
    "Octopus", "Pineapple", "Quokka", "Rhinoceros", "Snail", "Turtle", "Unicorn", "Vulture", "Walrus", "X-ray",
    "Yeti", "Zucchini", "Antelope", "Butterfly", "Crocodile", "Dinosaur", "Echidna", "Fox", "Gazebo", "Hammer",
    "Iguana", "Jaguar", "Kangaroo", "Lizard", "Meerkat", "Nightingale", "Ostrich", "Parrot", "Quail", "Raccoon",
    "Scorpion", "Toad", "Uakari", "Viper", "Weasel", "Xiphias", "Yellowjacket", "Zonkey", "Aardvark", "Bison", "Camel",
    "Donkey", "Elephant", "Falcon", "Gorilla", "Hyena", "Ibis", "Jackal", "Koala", "Lemur", "Meerkat", "Newt",
    "Ocelot", "Platypus", "Quokka", "Rattlesnake", "Seahorse", "Tarantula", "Uakari", "Vulture", "Wallaby", "X-ray",
    "Yak", "Zebra", "Alpaca", "Baboon", "Capybara", "Dhole", "Elephant", "Flamingo", "Gazelle", "Hamburger", "Ice cream",
    "Jigsaw", "Kangaroo", "Lemur", "Mongoose", "Nandu", "Okapi", "Pika", "Quokka", "Raccoon", "Seahorse", "Tiger",
    "Uakari", "Viper", "Wallaby", "Xenopus", "Yeti", "Zorilla", "Aardwolf", "Babirusa", "Capuchin", "Dhole", "Eel",
    "Flounder", "Gharial", "Hamster", "Ibis", "Jerboa", "Kakapo", "Lemur", "Mongoose", "Nandu", "Okapi", "Pika",
    "Quokka", "Rhea", "Snail", "Tapir", "Uguisu", "Vulture", "Wallaroo", "X-ray tetra", "Yak", "Zorse", "Axolotl",
    "Barracuda", "Chameleon", "Dugong", "Echidna", "Flamingo", "Gila monster", "Hedgehog", "Iguana", "Jellyfish", "Kangaroo",
    "Lemur", "Mantis", "Narwhal", "Ocelot", "Peacock", "Quokka", "Raccoon", "Seahorse", "Tiger", "Uakari", "Vulture",
    "Wallaby", "X-ray fish", "Yak", "Zebra", "Angelfish", "Bison", "Clownfish", "Dachshund", "Elephant", "Flamingo",
    "Gorilla", "Heron", "Ibis", "Jackal", "Koala", "Lemur", "Manatee", "Newt", "Ostrich", "Peacock", "Quokka", "Raccoon",
    "Seahorse", "Tiger", "Uakari", "Vulture", "Wallaby", "X-ray fish", "Yak", "Zebra", "Ant", "Bison", "Catfish", "Dhole",
    "Elephant", "Flamingo", "Gazelle", "Hippo", "Ibis", "Jackal", "Koala", "Lemur", "Meerkat", "Numbat", "Ostrich", "Peacock",
    "Quokka", "Raccoon", "Seahorse", "Tiger", "Uakari", "Vulture", "Wallaby", "Xenopus", "Yak", "Zebra", "Axolotl", "Badger",
    "Cobra", "Dalmatian", "Emu", "Falcon", "Giraffe", "Hamster", "Iguana", "Jackal", "Koala", "Lemur", "Manatee", "Newt",
    "Ostrich", "Peacock", "Quokka", "Raccoon", "Seahorse", "Tiger", "Uakari", "Viper", "Wallaby", "Xenopus", "Yeti", "Zorilla",
    "Aardwolf", "Babirusa", "Capuchin", "Dhole", "Eel", "Flounder"
]




from collections import defaultdict

gorupword = defaultdict(list)

# for word in random_words:
#     gorupword[word[0]].append(word)

print(gorupword)

# gorupword={}

for word in random_words:
    gorupword.setdefault(word[0], []).append(word)

print(gorupword)


import functools

@functools.cache
def climbStairs(n: int) -> int:
    @functools.cache
    def count(n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return count(n-1) + count(n-2)
    return count(n)


print(climbStairs(20))

import time, icecream

class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        total = 0
        while n != 1:
            time.sleep(0.3)
            icecream.ic(n)
            
            if n % 2:
                total += (x:=(n-1)//2)
                n = x + 1
            else:
                n //= 2
                icecream.ic(total)
                total += n
            icecream.ic(total)
        return total or 1

print(Solution().numberOfMatches(7))