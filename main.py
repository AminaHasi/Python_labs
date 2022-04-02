# Гасимова Аміна 141 група
# Лабороторна робота №1
# 5.Обчислити дробову частину середнього геометричного трьох заданих позитивних чисел.
import math


def average_value(num1, num2, num3):
    if num1 and num1 and num3 > 0:
        geom = math.pow(num1 * num2 * num3, 1 / 3)
        print(geom)
    else:
        print("Ви ввели неправильні числа. Введіть числа >0")


a = int(input("5.Введіть число 1: "))
b = int(input("Введіть число 2: "))
c = int(input("Введіть число 3: "))
average_value(a, b, c)
