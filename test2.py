
# Добавить "#" перед """ Start и """ End для задания 2-3-4-5

# Задание 1
# Пользователь вводит с клавиатуры три цифры. Необ-
# ходимо создать число, содержащее эти цифры. Например,
# если с клавиатуры введено 1, 5, 7, тогда нужно сформи-
# ровать число 157.

# """
#START_1
user_numbers = input("Введите 3 числа через пробел: ")
def task1(numbers):
    list = []

    for number in numbers.split():
        list.append(number)

    result = "".join(list)
    return int(result)

print("Результат:", task1(user_numbers))
#END_1
# """

"""
#START_1(2)
list2 = [int(input("Введите число 1: ")),int(input("Введите число 2: ")),int(input("Введите число 3: "))]
string_list = [str(x) for x in list2] 
joined_str = "".join(string_list)
result = int(joined_str)
print(result)
#END_1(2)
"""


# Задание 2
# Пользователь вводит с клавиатуры число, состоящее
# из четырех цифр. Требуется найти произведение цифр.
# Например, если с клавиатуры введено 1324, тогда резуль-
# тат произведения 1*3*2*4 = 24.

"""
#START_2
digits1 = int(input("Введите 4х значное число: "))
def task2(numbers):
    result = 1
    for x in str(numbers):
        result *= int(x)
    return result
print(task2(digits1))
#END_2
"""

# Задание 3
# Пользователь вводит с клавиатуры количество метров.
# Требуется вывести результат перевода метров в сантиме-
# тры, дециметры, миллиметры, мили.

"""
#START_2
metres1 = int(input("Введите длину в метрах: "))
def len1(number):
    cm = number * 100
    dm = number * 10
    mm = number * 1000
    miles = number * 0.00062
    print(f"{number} М = {cm}см / {dm}дм / {mm}мм / {miles} миль.")

len1(metres1)
#END_2
"""

# Задание 4
# Напишите программу, вычисляющую площадь тре-
# угольника. Пользователь вводит размер
# основания треугольника и размер высоты.

"""
#START_2

len = float(input("Введите длину основания треугольника: "))
height = float(input("Введите высоту треугольника: "))

def triangle_S(number1, number2):
    return 0.5 * number1 * number2

print("Площадь треугольника: ", triangle_S(len,height), "см")

#END_2
"""

# Задание 5
# Пользователь с клавиатуры вводит четырехзначное
# число. Необходимо перевернуть число и отобразить
# результат. Например, если введено 4512, результат 2154.

"""
#START_2
digit3 = int(input("Введите 4х значное число: "))

def backward_digit(number):
    return int(str(number)[::-1])

print(backward_digit(digit3))
#END_2
"""