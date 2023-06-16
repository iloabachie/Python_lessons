import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = datetime.date.today().year - birth_year
        return cls(name, age)

person = Person("Alice", 25)
person_from_birth_year = Person.from_birth_year("Bob", 1985)

'''
print(type(person_from_birth_year))
print(type(person))

print(person_from_birth_year.age, person_from_birth_year.name)

import ConsolePrint as prt

prt.text_box("hello testing this", format='red', padding=True)

prt.printing("animated text", format='green')

prt.star_square(10, format="yellow_bg")

prt.asteriskify("i will become a programmer one day", format='cyan')

prt.text_box("box here")

# prt.startConsoleSave()

print(prt.__name__)

# prt.endConsoleSave()
'''

print(r'xCo\deC\c\'ker\eco\\rds.json')

print('\ ', type(person_from_birth_year), type(45), type("hello"), type(person))