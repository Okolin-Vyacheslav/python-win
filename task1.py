def exe_1(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'На ноль делить нельзя'


print(exe_1((int(input('Введите число а: '))), (int(input('Введите число b:  ')))))
