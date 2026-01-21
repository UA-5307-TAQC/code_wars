"""Solutions for 8 kyu tasks"""

import math

from core import kata  # pylint: disable=import-error


@kata("Keep Hydrated!")
def liters(time):
    """Return rounded amount of water."""
    return time // 2


@kata("Volume of a Cuboid")
def get_volume_of_cuboid(length, width, height):
    """Calculate volume of cuboid."""
    volume = length * width * height
    return volume


@kata("Miles per gallon to kilometers per liter")
def converter(mpg):
    """Convert mpg into kpl"""
    imperial_gallon = 4.54609188  # litres
    mile = 1.609344  # kilometres
    kpl = mpg * mile / imperial_gallon
    return round(kpl, 2)


@kata("To square(root) or not to square(root)")
def square_or_square_root(arr):
    """square root or square the number."""
    result = [math.sqrt(i) if math.sqrt(i).is_integer() else pow(i, 2) for i in arr]
    return result


@kata("Count of positives / sum of negatives")
def count_positives_sum_negatives(arr):
    """Count of positives / sum of negatives."""
    if arr:
        count_pos = sum(1 for i in arr if i > 0)
        sum_neg = sum(i for i in arr if i < 0)
        result = [count_pos, sum_neg]
        return result
    return arr


@kata("Convert a String to a Number!")
def string_to_number(s):
    """Convert string to number."""
    return int(s)


@kata("Am I Wilson")
def am_i_wilson(n):
    """Wilson primes."""
    if n > 2:
        return (math.factorial(n - 1) + 1) % n**2 == 0
    return False


@kata("Formatting decimal places #0")
def two_decimal_places(n):
    """Round to two decimal places."""
    return round(n, 2)


@kata("Find numbers which are divisible by given number")
def divisible_by(numbers, divisor):
    """Find numbers which are divisible by given number."""
    result = [i for i in numbers if i % divisor == 0]
    return result
