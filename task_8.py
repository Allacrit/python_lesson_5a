"""
Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
"""
a = int(input('Введите первое число A = '))
b = int(input('Введите второе число B = '))


def func2(a, b):
    result = a
    if b == 1:
        return result
    return result * func2(a, b - 1)


print(f'{a} в степени {b} = {func2(a, b)}')
