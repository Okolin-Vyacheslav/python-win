user_input = input('Введите предложение: ')
user_input = user_input.split()

for key, item in enumerate(user_input):
    print(key + 1, item[0:11])
