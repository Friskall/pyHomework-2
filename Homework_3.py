# Задание 1
# Пользователь вводит с клавиатуры число. Необходимо проверить его на четность и нечетность.
# Если число четное требуется вывести на экран число и надпись Even number.
# Если число нечетное выведите на экран число и надпись Odd number.

#"""
# ___START 1___

digit1 = int(input("Введите число: "))

def check1(num):
    if 0 == num%2:
        return "Even number"
    else:
        return "Odd number"

print(check1(digit1))

# ___END 1___
#"""
from random import choice

# Задание 2
# Пользователь вводит с клавиатуры число.
# Необходимо проверить его на кратность 7.
# Если число кратно требуется вывести на экран число и надпись Number is multiple 7.
# Если число не кратно выведите на экран число и надпись Number is not multiple 7.

#"""
# ___START 2___

digit2 = int(input("Введите число: "))

def check2(num):
    if 0 == num%7:
        return "Number is multiple 7"
    else:
        return "Number is not multiple 7"

print(check2(digit2))

# ___END 2___
#"""

# Задание 3
# Пользователь вводит с клавиатуры два числа.
# Необходимо найти максимум из двух чисел и показать его на экран.

#"""
# ___START 3___

digits3 = [
    int(input("Введите 1е число: ")),
    int(input("Введите 2е число: "))]

def check3(num):
    return max(num)

print(check3(digits3))

# ___END 3___
#"""

# Задание 4
# Пользователь вводит с клавиатуры два числа.
# Необходимо найти минимум из двух чисел и показать его на экран.

#"""
# ___START 4___
digits4 = [
    int(input("Введите 1е число: ")),
    int(input("Введите 2е число: "))]


def check4(num):
    return min(num)

print(check4(digits4))

# ___END 4___
#"""

# Задание 5
# Пользователь вводит с клавиатуры два числа.
# В зависимости от выбора пользователя нужно показать сумму двух чисел,
# разницу двух чисел, среднеарифметическое или произведение двух чисел.

#"""
# ___START 5__
digits5 = [
    int(input("Введите 1е число: ")),
    int(input("Введите 2е число: "))]
user_choise1 = input("Выберите действие: '+' / '-' / 'avg' / '*' ")

def check5(num,choise):
    result = 0
    if choise == '+':
        result = num[0] + num[1]
    elif choise == '-':
        result = num[0] - num[1]
    elif choise == 'avg':
        result = (num[0] + num[1]) / len(num)
    else:
        result = num[0] * num[1]

    return int(result)

print(check5(digits5, user_choise1))

# ___END 5__
#"""