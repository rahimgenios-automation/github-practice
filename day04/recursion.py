def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)


def reverse(string):
    if len(string) <= 0:
        return string
    return string[-1] + reverse(string[:-1])

reverse("hello")

string = "hello"
print(string[:-1])