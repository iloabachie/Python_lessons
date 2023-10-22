class User:
    print('lets test this')

    def __init__(self, user_id, user_name, followers=0, following=0):
        print('new user created')
        self.user_id = user_id
        self.user_name = user_name
        self.followers = followers
        self.following = following
        self.followed_list = []
        self.followers_list = []

    def follow(self, user):        
        self.followed_list.append(user.user_name)
        user.followers_list.append(self.user_name)
        user.followers = len(user.followers_list)
        self.following = len(self.followed_list)
        

    def unfollow(self, user):        
        self.followed_list.remove(user.user_name)
        user.followers_list.remove(self.user_name)
        user.followers = len(user.followers_list)
        self.following = len(self.followed_list)


user_1 = User('003', 'angela')

user_2 = User('001', 'meuzue')

user_3 = User('234', 'ronaldo')

print(f'{user_1.user_name} has followers = {user_1.followers}, following = {user_1.following}')
print(f'{user_2.user_name} has followers = {user_2.followers}, following = {user_2.following}')
print(f'{user_3.user_name} has followers = {user_3.followers}, following = {user_3.following}')
print('-----------------\n')

for x in range(15):
    user_1.follow(user_2)
    user_1.follow(user_3)
    user_2.follow(user_3)
    user_3.follow(user_1)

print(f'{user_1.user_name} has followers = {user_1.followers}, following = {user_1.following}')
print(f'{user_2.user_name} has followers = {user_2.followers}, following = {user_2.following}')
print(f'{user_3.user_name} has followers = {user_3.followers}, following = {user_3.following}')
print(user_1.followers_list, user_1.followed_list)
print('-----------------\n')
print(user_2.followers_list, user_2.followed_list)
print('-----------------\n')
print(user_3.followers_list, user_3.followed_list)
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


print(user_1.followers_list, user_1.followed_list)
print('-----------------\n')
print(user_2.followers_list, user_2.followed_list)
print('-----------------\n')
print(user_3.followers_list, user_3.followed_list)
print('-----------------\n')