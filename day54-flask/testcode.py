class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False
    
    def is_authenticated_decorator(function):
        def wrapper(*args, **kwargs):
            if args[0].is_logged_in:
                function(*args)
            else:
                print(f'{args[0].name} needs to log in first')
        return wrapper
    
    def log_decorator(function):
        def wrapper(*args):
            print(f"you called {function.__name__} and it took {[args[0].name]} and returned{function(*args)}")
        return wrapper
    
    
    @is_authenticated_decorator
    @log_decorator
    def creat_blog_post(self, user):
        if user.is_logged_in:
            print(f' This blog is created by {user.name}')
        
            
            
new_user = User("Nkem")

new_user.is_logged_in = True

new_user.creat_blog_post(new_user)


# ----------------------------------------------

# Create the logging_decorator() function 👇

def logging_decorator(funct):
    def wrapper(*args):
        print(f'You called {funct.__name__}{tuple([*args])}\nIt returned: {funct(*args)}')
    return wrapper


# Use the decorator 👇

@logging_decorator
def add(*args):
    return sum([*args])

add(1)
