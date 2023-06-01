from time import time

def timer(funct):
    '''This function is a decorator that calculates the time taken to run a function.'''
    def wrapper(*args, **kwargs):        
        start = time()
        funct(*args, **kwargs)
        print(f'** "{funct.__name__}" ran in {time() - start} seconds')
    return wrapper



import shutil

terminal_width, _ = shutil.get_terminal_size()

if __name__ == "__main__":
    print("Terminal width:", terminal_width, _)


import os

print(os.get_terminal_size())


