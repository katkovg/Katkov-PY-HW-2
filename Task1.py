# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
def countDigitsSum (number):
    digitsSum = 0
    while number > 0:
        lastDigit = number % 10
        digitsSum += lastDigit 
        number //= 10
    return digitsSum


number = float(input('Введите вещественное число: '))
digitsSum = 0
lastDigit = 0
if int(number) == number:
    digitsSum = countDigitsSum(number)
    print('Сумма цифр составляет: ' + digitsSum)
else:
    while int(number) != number:
        number *= 10
    digitsSum = countDigitsSum(number)
    print('Сумма цифр составляет: ' + digitsSum)