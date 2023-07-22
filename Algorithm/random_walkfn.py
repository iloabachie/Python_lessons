import random
def random_walk(n):
    """ return coordinates after."""
    x = y = 0       
    for _ in range(n):
        dx, dy = random.choice([(0,1), (1,0), (0,-1), (-1,0)])
        x += dx
        y += dy
    return abs(x), abs(y)

more_than_4 = []
less_eq_4 = []
for x in range(50):
    distance = sum(random_walk(50))
    if distance <= 10: less_eq_4.append(distance)
    else: more_than_4.append(distance)

print(more_than_4, len(more_than_4))
print(less_eq_4, len(less_eq_4))


number_of_walks = 300
block_target = 5

for walk_length in range(1, 51):
    no_transport = 0
    for i in range(number_of_walks):
        distance = sum(random_walk(walk_length))
        if distance < block_target:
            no_transport += 1
    no_transport_percent = no_transport / number_of_walks *100
    print(f'walk size: {walk_length}, target: {block_target} the % is {no_transport_percent}%')
    
    
class Person():
    ...

user1 = Person()
user1.fname = "john"
user1.lname = "poole"
user1.lnames = "poole"

print(user1.__sizeof__())
