from functools import reduce
print([el for el in range(100, 1001) if el % 2 == 0])
print(reduce(lambda x, y: x * y, [el for el in range(100, 1001) if el % 2 == 0]))