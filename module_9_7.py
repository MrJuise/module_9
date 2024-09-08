'''
Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:
Напишите 2 функции:

    Функция, которая складывает 3 числа (sum_three)
    Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом
    и "Составное" в противном случае.
'''

def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        c = 0
        for i in range(1, n + 1):
            if n % i == 0:
                c += 1
        if c == 2:
            print("Простое число")
        else:
            print("Число составное")

        return n
    return wrapper


@is_prime
def sum_three(a, b, c):
    summ = a + b + c
    return summ


result = sum_three(1, 1, 5)
print(result)