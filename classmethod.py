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



prt.text_box("hello testing this", format='red_bg')


prt.printing("animated text", format='green')

prt.star_square(10, format="green_bg")