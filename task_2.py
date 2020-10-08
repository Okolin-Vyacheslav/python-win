
my_list = [1, 2, 3, 4, 5,]

count = 0
for i in range(int(len(my_list) / 2)):
    my_list[count], my_list[count + 1] = my_list[count + 1], my_list[count]
    count += 2

print(my_list)