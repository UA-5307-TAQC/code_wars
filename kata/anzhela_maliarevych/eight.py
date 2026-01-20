"""8kyu tasks"""

import re
from math import sqrt
import math


def litres(time):
    """Keep Hydrated."""
    a = int(time * 0.5)
    return a


def get_volume_of_cuboid(length, width, height):
    """Volume of a Cuboid."""
    volume = length * width * height
    return volume


def converter(mpg):
    """Miles per gallon to kilometers per liter."""
    return round(mpg * 1.609344 / 4.54609188, 2)


def square_or_square_root(arr):
    """To square(root) or not to square(root)."""
    result = []
    
    for x in arr:
        root = math.sqrt(x)
        if root.is_integer():
            result.append(int(root))
        else:
            result.append(x * x)
    return result


def count_positives_sum_negatives(arr):
    """Count of positives / sum of negatives."""
    result = []

    result.append(sum(x > 0 for x in arr))
    result.append(sum(x for x in arr if x < 0))

    if not arr:
        return []

    return result


def string_to_number(s):
    """Convert a String to a Number."""
    return int(s)


def am_i_wilson(n):
    """Wilson primes."""
    if n < 2:
        return False
    result = (math.factorial(n - 1) + 1) % (n * n) == 0
    return result


def two_decimal_places(n):
    """Format decimal places."""
    return round(n, 2)


def divisible_by(numbers, divisor):
    """Find numbers which are divisible by given number."""
    result = []
    
    for n in numbers:
        if n % divisor == 0:
            result.append(n)
    return result