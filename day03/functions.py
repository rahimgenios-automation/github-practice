def normalize_score(score):
    return score / 100


result = normalize_score(85)

print(result)
print(type(result))



def salary_calculator(base, hours):
    return base * hours


Sajid = salary_calculator(100, 12)

def positional_function(x, /):
    return x

def keyword_function(*, x):
    return x



keyword_function(y = 10)

def my_function(*kids):
    return kids[1]
    
my_function("Sajid", "Almas")

def emp_function(greeting, *kids):
    for x in kids:
        print(greeting + " " + x)

emp_function("Hello", "Sajid", "Majid")


def some_function(username, **details):
    print("Username: ", username)
    print("Additional Details")
    for key, value in details.items():
        print(key, ":", value)

some_function("Abdul Rahim", age = 21, gender = "male")


x = 0
def function(z):
    global x
    while x < 5:
        print(x)
        x = x +1
    return z


@function
def newfunction():
    return "This is the additional functionality"

print(newfunction())