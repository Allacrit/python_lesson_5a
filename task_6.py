"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""


def func(number, count=10):
    print(f'Количество попыток: {count}')
    if count < 0:
        print(f"Число не отгадано. Загаданное число: {number}")
        return number
    user_number = int(input('Введите число: '))
    if user_number == number:
        print(f'^^^Ты угадал! Это число {number}!!!^^^')
        return user_number
    elif user_number > number:
        print(
            f'Твое число {user_number} больше загаданного!')
        return func(number, count - 1)
    else:
        print(
            f'Твое число {user_number} меньше загаданного!')
        return func(number, count - 1)


from random import randint

number = randint(0, 100)

func(number)
