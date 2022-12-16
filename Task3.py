# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для получения случайного int

import random

test_list = [5, 6, 7, 8, 9, 10, 11]

print ("Изначальная версия списка: " + str(test_list))

for i in range(len(test_list)-1, 0, -1):
        j = random.randint(0, i + 1)
        temp = test_list[i]
        test_list[i] = test_list[j]
        test_list[j] = temp

print ("Перемешанная версия списка: " + str(test_list))