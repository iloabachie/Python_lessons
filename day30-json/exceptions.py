fruits = ['apple', 'pear', 'orange']

def make_pie(index):
    try:
        fruit = fruits[index]
          
    except KeyError as error1:
        print(f'sorry we had a {error1} error')
    except IndexError as error2:
        print(f'sorry we had a {error2} error')
    else:
        print(fruit + 'pie') 
    finally:
        print('would you like another pie')

make_pie(2)
# ---------------------------------------------------------------

fruits = ['apple', 'pear', 'orange']

def make_pie(index):
    fruit = fruits[index]
    print(fruit + 'pie') 

make_pie(5)

# ----------------------------------------------------------
facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0
maxi = []

for post in facebook_posts:
    try:
        total_likes += post['Likes']
    except KeyError:
        pass
print(total_likes)

# -----------------------------------------------------------------

