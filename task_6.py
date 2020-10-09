def exe_6(text):
    my_text = []
    for i in range(len(text)):
        my_text.append(text[i][0:1].title() + text[i][1:])
    return ' '.join(my_text)


print(exe_6(input('Введите текст: ').split()))
