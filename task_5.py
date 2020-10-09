end_word = "$"
summ = 0
to_exit = False
while not to_exit:
    next_input = input('\n')
    numbers = next_input.split()
    for num in numbers:
        if num == end_word:
            to_exit = True
            break
        try:
            num = int(num)
        except ValueError:
            continue

        summ += num

    print(f'Сумма - {summ}')
