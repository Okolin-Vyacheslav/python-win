from sys import argv

script_name, time, salary = argv
try:
    time = int(time)
    salary = int(salary)
    total = time * salary
    bonus = (total / 100) * 20
    total_var = total + bonus
    print('Ваш оклад: ', total)
    print('Ваша премия: ', bonus)
    print('Ваша зарплата состаявляет: ', total_var)
except ValueError:
    print('Данные некорректны')



#
# print('Иммя скрипта:', script_name)
# print('Выработка в часах: ', float(time))
# print('Оклад по должности в час: ', float(salary))
# print('Премия по итогам работы: ', float(bonus))
# print('Зп составила:', res(time * salary + bonus))
# def sal(**kwargs):
#     total = time * salary
#     bonus = (total / 100) * 20
#     total_var = total + bonus
#     print(bonus)
#     print(total_var)
#
#
# print(sal(time, salary))
#  TODO: и это самая малая часть закомментирована, вариаций было много, но все были не правильные=). За минут 40
#  TODO: перелапатил много инфы, а подсказка была в конце вебинара 4го=)