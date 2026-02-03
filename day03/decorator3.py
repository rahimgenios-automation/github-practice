def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("A")
        value = func(*args, **kwargs)
        print("B")
        return value
    return wrapper

@my_decorator
def test():
    print("C")

test()
