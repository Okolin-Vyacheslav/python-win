seasons = {'Зима': [12, 1, 2],
           'Весна': [3, 4, 5],
           'Лето': [6, 7, 8],
           'Осень': [9, 10, 11],
           }
user_input = int(input('Введите номер месяца: '))
for key in seasons.keys():
    if user_input in seasons[key]:
        print(key)

# TODO: Не знаю как сделать со списком.
