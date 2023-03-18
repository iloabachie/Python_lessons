import time
current_time = time.time()
# print(current_time)

def speed_calc_decorator(funct):
    def wrapper():
        current_time = time.time()
        funct()
        print(f'{funct.__name__} run speed: {time.time() - current_time}')
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator   
def slow_function():
    for i in range(100000000):
        i * i


# fast_function()
# slow_function()

speed_calc_decorator(slow_function)()

# slow()