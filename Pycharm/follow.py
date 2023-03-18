class User:
    print('lets test this')

    def __init__(self, user_id, user_name, followers=0, following=0):
        print('new user created')
        self.user_id = user_id
        self.user_name = user_name
        self.followers = followers
        self.following = following

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def unfollow(self, user):
        user.followers -= 1
        self.following -= 1


user_1 = User('003', 'angela')

user_2 = User('001', 'meuzue')

user_3 = User('234', 'ronaldo', 8, 3)

print(f'{user_1.user_name} has followers = {user_1.followers}, following = {user_1.following}')
print(f'{user_2.user_name} has followers = {user_2.followers}, following = {user_2.following}')
print(f'{user_3.user_name} has followers = {user_3.followers}, following = {user_3.following}')
print('-----------------\n')

user_1.follow(user_2)
user_1.follow(user_3)
user_2.follow(user_3)

print(f'{user_1.user_name} has followers = {user_1.followers}, following = {user_1.following}')
print(f'{user_2.user_name} has followers = {user_2.followers}, following = {user_2.following}')
print(f'{user_3.user_name} has followers = {user_3.followers}, following = {user_3.following}')
print('-----------------\n')

user_2.follow(user_1)

print(f'{user_1.user_name} has followers = {user_1.followers}, following = {user_1.following}')
print(f'{user_2.user_name} has followers = {user_2.followers}, following = {user_2.following}')
print(f'{user_3.user_name} has followers = {user_3.followers}, following = {user_3.following}')
print('-----------------\n')

user_2.unfollow(user_1)

print(f'{user_1.user_name} has followers = {user_1.followers}, following = {user_1.following}')
print(f'{user_2.user_name} has followers = {user_2.followers}, following = {user_2.following}')
print(f'{user_3.user_name} has followers = {user_3.followers}, following = {user_3.following}')
print('-----------------\n')

user_3.unfollow(user_1)
print(f'{user_1.user_name} has followers = {user_1.followers}, following = {user_1.following}')
print(f'{user_2.user_name} has followers = {user_2.followers}, following = {user_2.following}')
print(f'{user_3.user_name} has followers = {user_3.followers}, following = {user_3.following}')
