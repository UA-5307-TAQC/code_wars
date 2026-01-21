"""Solutions for 8 kyu tasks."""

import math

from core import kata  # pylint: disable=import-error


@kata("Keep Hydrated!")
def keep_hydrated(time):
    """Keep Hydrated! solution."""
    return int(time * 0.5)


@kata("Volume of a Cuboid")
def get_volume_of_cuboid(length, width, height):
    """Volume of cuboid solution."""
    return length * width * height


@kata("Miles per gallon to kilometers per liter")
def converter(mpg):
    """Miles per gallon to kilometres per liter solution."""
    return round(mpg * 1.609344 / 4.54609188, 2)


@kata("To square(root) or not to square(root)")
def square_or_square_root(arr: list[int]):
    """To square root or no to square solution."""
    return [int(num**0.5) if (num**0.5 % 1 == 0) else num**2 for num in arr]


@kata("Count of positives / sum of negatives")
def count_positives_sum_negatives(arr: list[int]):
    """Count of positives / sum of negatives solution."""
    if not arr:
        return []
    count_pos = 0
    sum_neg = 0
    for num in arr:
        if num > 0:
            count_pos += 1
        else:
            sum_neg += num
    return [count_pos, sum_neg]


@kata("Convert a String to a Number!")
def string_to_number(s):
    """Convert a String to a Number solution."""
    return int(s)


@kata("Am I Wilson")
def am_i_wilson(n):
    """Wilson primes solution."""
    if 2 <= n <= 563:
        return (math.factorial(n - 1) + 1) % (n * n) == 0
    return False


@kata("Formatting decimal places #0")
def two_decimal_places(n):
    """Format decimal places solution."""
    return round(n, 2)


@kata("Find numbers which are divisible by given number")
def divisible_by(numbers: list[int], divisor: int):
    """Find numbers which are divisible by given number solution."""
    return [num for num in numbers if num % divisor == 0]
