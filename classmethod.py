import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.zzz = "hello"

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = datetime.date.today().year - birth_year
        return cls(name, age)

person = Person("Alice", 25)
person_from_birth_year = Person.from_birth_year("Bob", 1985)
print(person_from_birth_year.age)


print('\ ', type(person_from_birth_year), type(45), type("hello"), type(person))

import requests
response = requests.get("https://api.npoint.io/88838b326e7274d04e53")    
response.raise_for_status()
data = response.json() 
print(type(data), len(data))
print(data[0])


from dataclasses import dataclass, field
import random, string

def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))

#@dataclass(frozen=True, kw_only=False)  #generates the initializer and the str dunder.  default is false but true means initi varialbes cannot be changed.
#takes only key word arguments.  
@dataclass
class Person:
    name:str
    address:str
    active:bool = True
    email_addresses: list[str] = field(default_factory=list)
    id:str = field(default_factory=generate_id)
    id_2:str = field(init=False, default_factory=generate_id) # takes it out of init variables
    # search_string:str = field(init=False, repr=False)  # not required as it is post init.
    
    def __post_init__(self) -> None:
        self.search_string = f'{self.name} {self.address}'

def make_person() -> None:
    person_a = Person("John", "Ling road", False)
    person_b = Person("Sheila", "barrie")
    print(person_a.search_string)
    print(person_b)
    print(person_b.__dict__)
    print(Person)
    
make_person()


from enum import Enum, auto

class Role(Enum):
    '''employee roles'''
    president = auto()
    vicepresident = auto()
    manager = auto()


print(type(Role.president))

class DimensionExceptionError(Exception):
    """Custom error when the terminal width is too small"""
    def __init__(self, error_message):
        # self.error_message = error_message
        super().__init__(error_message)
        

raise DimensionExceptionError("this is the error")

