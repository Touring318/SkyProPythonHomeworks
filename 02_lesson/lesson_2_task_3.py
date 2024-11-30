# Функция определения площади квадрата с округлением в большую сторону

import math


def square(side):
    area_of_the_square = side ** 2
    return area_of_the_square


side = float(input("Введите длину стороны квадрата: "))
print(math.ceil(square(side)))
