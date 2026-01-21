"""Solutions for Codewars kata (8 kyu)."""

import math

from core import kata  # pylint: disable=import-error


@kata("Keep Hydrated!")
def litres(time):
    """Keep Hydrated! exercise"""
    litres_count = math.floor(time / 2)
    return litres_count


@kata("Volume of a Cuboid")
def get_volume_of_cuboid(length, width, height):
    """Volume of a Cuboid exercise"""
    volume = length * width * height
    return volume


@kata("Miles per gallon to kilometers per liter")
def converter(mpg):
    """Miles per gallon to kilometers per liter exercise"""
    klp = round((mpg * 1.609344) / 4.54609188, 2)
    return klp


@kata("To square(root) or not to square(root)")
def square_or_square_root(arr):
    """To square(root) or not to square(root) exercise"""
    result = []
    for num in arr:
        if (math.sqrt(num)).is_integer():
            result.append(int(math.sqrt(num)))
        else:
            result.append(num**2)
    return result


@kata("Count of positives / sum of negatives")
def count_positives_sum_negatives(arr):
    """Count of positives / sum of negatives exercise"""
    result = []
    negative = 0
    positive = 0
    if arr:
        for num in arr:
            if num > 0:
                positive += 1
            elif num < 0:
                negative += num
        result.append(positive)
        result.append(negative)
    return result


@kata("Convert a String to a Number!")
def string_to_number(s):
    """Convert a String to a Number! exercise"""
    return int(s)


@kata("Am I Wilson")
def am_i_wilson(n):
    """Wilson primes exercise"""
    if n <= 1:
        return False

    # Примітка: Цей алгоритм є дуже неефективним для великих чисел через факторіал.
    # Проте для 8 kyu і обмежених тестів на Codewars це рішення проходить.
    # Відомі прості числа Вілсона: 5, 13, 563.
    return ((math.factorial(n - 1) + 1) / (n * n)).is_integer()


@kata("Formatting decimal places #0")
def two_decimal_places(n):
    """Formatting decimal places exercise"""
    return round(n, 2)


@kata("Find numbers which are divisible by given number")
def divisible_by(numbers, divisor):
    """Find numbers which are divisible by given number exercise"""
    result = []
    for num in numbers:
        if num % divisor == 0:
            result.append(num)
    return result
