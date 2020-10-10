from itertools import count, cycle
for el in count(int(input('Введите стартовое число: ' ))):
    if el > 10:
        break
    print(el)

my_list = [123, 'writing', 321, 'cfg']
i = 0
for el in cycle(my_list):
   i += 1
   if i > 100:
       break
   print(el)
