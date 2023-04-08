"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""

count_element = int(input('Введите количество элементов: '))
row_number = 1
sum_numbers = 0


def calculation(count_element, row_number, sum_numbers):
    if count_element > 0:
        count_element -= 1
        sum_numbers += row_number
        row_number = row_number / -2
        calculation(count_element, row_number, sum_numbers)
        return sum_numbers
    else:
        print(f'Сумма заданных элементов равна {sum_numbers}.')


calculation(count_element, row_number, sum_numbers)
