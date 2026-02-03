import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time Taken: ", end - start)
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(2)



slow_function()