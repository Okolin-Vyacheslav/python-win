def my_func(x, y):
    numbers = x ** y
    return numbers


print(my_func(2, 6))


def my_func2(x, y):
    for i in range(y - 1):
        x *= x
        return x


print(my_func(2, 6))
