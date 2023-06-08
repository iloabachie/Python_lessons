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


print(type(person_from_birth_year))
print(type(person))

print(person_from_birth_year.age, person_from_birth_year.name)





import ConsolePrint.animate as prt



prt.text_box("hello testing this", format='red', padding=True)


prt.printing("animated text", format='green')

prt.star_square(10, format="green_bg")

prt.asteriskify("i will become a programmer one day", format='cyan')

import colour_splash

colour_splash.colour("this is red text with a white background", "red", "white") or colour_splash.colour("this is red text with a white background", colour_splash.colours.red, colour_splash.colours.white)


prt.text_box("box here")

text = "code breaker"


def spread(string):
    string = list(string)
    string = ' '.join(string)
    print(string)


spread(text)