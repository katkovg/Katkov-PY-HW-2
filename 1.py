# Переворот массива
my_list = [1, 2, 3, 4, 5]

for i in range(len(my_list) // 2):
    n = (len(my_list) - 1) - i
    temp = my_list[i]
    my_list[i] = my_list[n]
    my_list[n] = temp

print(my_list)

# Пузырьковая сортировка

my_list = [2, 1, 3, 10, 5, 4, 9, -32, -45, 76, -17]

for i in range(len(my_list)-1):
    for j in range(len(my_list)-1):
        if my_list[j] > my_list[j+1]:
            temp = my_list[j]
            my_list[j] = my_list[j+1]
            my_list[j+1] = temp
print(my_list)