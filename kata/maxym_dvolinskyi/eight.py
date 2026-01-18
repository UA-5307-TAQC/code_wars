"""Solutions for 8 kyu tasks"""

import math


def liters(time):
    """Ruturn rounded amount of water."""
    return time // 2


def get_volume_of_cuboid(length, width, height):
    """Calculate volume of cuboid."""
    volume = length * width * height
    return volume


def converter(mpg):
    """Convert mpg into kpl"""
    imperial_gallon = 4.54609188  # litres
    mile = 1.609344  # kilometres
    kpl = mpg * mile / imperial_gallon
    return round(kpl, 2)


def square_or_square_root(arr):
    """square root or square the number."""
    result = [math.sqrt(i) if math.sqrt(i).is_integer() else pow(i, 2) for i in arr]
    return result


def count_positives_sum_negatives(arr):
    """Count of positives / sum of negatives."""
    if arr:
        count_pos = sum(1 for i in arr if i > 0)
        sum_neg = sum(i for i in arr if i < 0)
        result = [count_pos, sum_neg]
        return result
    return arr


def string_to_number(s):
    """Convert string to number."""
    return int(s)


def am_i_wilson(n):
    """Wilson primes."""
    if n > 2:
        return (math.factorial(n - 1) + 1) % n**2 == 0
    return False


def two_decimal_places(n):
    """Round to two decimal places."""
    return round(n, 2)


def divisible_by(numbers, divisor):
    """Find numbers which are divisible by given number."""
    result = [i for i in numbers if i % divisor == 0]
    return result
