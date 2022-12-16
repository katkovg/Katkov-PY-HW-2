# Задайте список из n чисел последовательности (1 + 1/n)^n, выведете его на экран, а так же сумму элементов списка.
n = int(input('Введите число: '))

values_sum = 0
task_list = []

for i in range(1, n+1):
    value = (1 + (1 / i))**i
    values_sum += value
    task_list.append(value)

print(f'Список чисел последовательности (1+(1/{n}))^{n} --->>> ' + str(task_list)[1:-1])
print('Сумма элементов списка: ' + str(values_sum))