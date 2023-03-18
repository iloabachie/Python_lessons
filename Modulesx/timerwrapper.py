

def timer(funct):
    '''This function is a decorator that calculates the time taken to run a function.'''
    def wrapper(*args, **kwargs):
        from time import time
        start = time()
        funct(*args, **kwargs)
        print(f'** "{funct.__name__}" ran in {time() - start} seconds')
    return wrapper