from random import choice
import sys

for p in sys.path:
  print(p)

sys.path.append('day14')

from art_day_14 import logo, vs
from game_data14 import data

def game():
    def clear():
        from os import system
        return system('cls ')

    clear()

    print('Thank you for playing')
    print(logo)
    print('''Instructions choose a or b to select who is bigger\n\n''')

    def b_xter():
        b = choice(data)
        while b == a:
            b = choice(data)
        return b

    a = choice(data)
    b = b_xter()
    print(f"Compare {a['name']}, \nwho is a {a['description']}\n from \n{a['country']}\n",
          f'{vs}\n', f"Compare {b['name']},\nwho is a {b['description']}\nfrom {b['country']}")

    selection = input('a or b: ').lower()

    count = 0
    # result = a['follower_count'] > b['follower_count']
    while selection == 'a' and (a['follower_count'] > b['follower_count']) or selection == 'b' and not (a['follower_count'] > b['follower_count']):
        count += 1
        clear()
        print(f"current streak: {count}")
        a = b
        b = b_xter()

        print(logo)
        print(f"Compare {a['name']}, who is a {a['description']} from {a['country']}\n",
              f'{vs}\n', f"Compare {b['name']}, who is a {b['description']} from {b['country']}")
        selection = input('a or b: ').lower()

    print(f'sorry you lose after streak: {count}')
    print('Thank you for playing')


game()
