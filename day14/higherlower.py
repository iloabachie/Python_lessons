from random import choice
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States'
    }]
logo = """
            __  ___       __             
        / / / (_)___ _/ /_  ___  _____
        / /_/ / / __ `/ __ \/ _ \/ ___/
        / __  / / /_/ / / / /  __/ /    
        /_/ ///_/\__, /_/ /_/\___/_/     
        / /  /____/_      _____  _____
        / /   / __ \ | /| / / _ \/ ___/
        / /___/ /_/ / |/ |/ /  __/ /    
        /_____/\____/|__/|__/\___/_/     
"""

vs = """
            _    __    
            | |  / /____
            | | / / ___/
            | |/ (__  ) 
            |___/____(_)
            """


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
