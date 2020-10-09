name1 = input('Введите имя: ')
surname1 = input('Введите фамилию: ')
year1 = input('Введите сколько вам лет: ')
city1 = input('Введите город, в котором проживаете: ')
email1 = input('Введите Ваш email: ')
telephone1 = input('Введите номер телефона: ')


def my_func(surname=surname1, name=name1, year=year1, city=city1, email=email1, telephone=telephone1):

    return (', '.join([name1, surname1, year1, city1, email1, telephone1]))


print(my_func())
