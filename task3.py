def max_sum(a, b, c):
    number = [a, b, c]
    number.remove(min(a, b, c))
    return sum(number)


print(max_sum(3, 4, 6))
