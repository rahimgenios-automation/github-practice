def say_hi():
    print("Hi!")

def my_decorator(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function")
    return wrapper


say_hi = my_decorator(say_hi)

say_hi()


@my_decorator
def say_hi():
    print("Hi!")

say_hi = my_decorator(say_hi)
say_hi()