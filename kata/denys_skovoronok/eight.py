"""File for solving CodeWars 8kyu tasks."""

import math as m

from core import kata  # pylint: disable=import-error


@kata("Keep Hydrated!")
def litres(time):
    """Calculate litres based on time."""
    return int(time * 0.5)


@kata("Volume of a Cuboid")
def get_volume_of_cuboid(length, width, height):
    """Calculate volume of cuboid."""
    return length * width * height


@kata("To square(root) or not to square(root)")
def square_or_square_root(arr):
    """To square root or no to square."""
    result = [m.sqrt(i) if m.sqrt(i).is_integer() else i**2 for i in arr]
    return result


@kata("Count of positives / sum of negatives")
def count_positives_sum_negatives(arr):
    """Count of positives / sum of negatives."""
    if not arr:
        return []

    neg = sum(i for i in arr if i < 0)
    pos = sum(1 for i in arr if i > 0)

    result = [pos, neg]
    return result


@kata("Convert a String to a Number!")
def string_to_number(s):
    """Convert string to number."""
    return int(s)


@kata("Am I Wilson")
def am_i_wilson(n):
    """Check if number is Wilson prime."""
    if n < 2:
        return False

    return (m.factorial(n - 1) + 1) % n**2 == 0


@kata("Formatting decimal places #0")
def two_decimal_places(n):
    """Round number to two decimal places."""
    return round(n, 2)


@kata("Find numbers which are divisible by given number")
def divisible_by(numbers, divisor):
    """Filter numbers divisible by divisor."""
    result = [i for i in numbers if i % divisor == 0]
    return result
