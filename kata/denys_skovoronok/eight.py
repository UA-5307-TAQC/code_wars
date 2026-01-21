"""File for solving CodeWars 8kyu tasks."""

import math as m


def litres(time: float):
    """Calculate litres based on time."""
    return int(time * 0.5)


def run_litres():
    """Run litres function based on time."""
    time = float(input("Enter time: "))
    return litres(time)


def get_volume_of_cuboid(length: float, width: float, height: float):
    """Calculate volume of cuboid."""
    return length * width * height


def square_or_square_root(arr: list):
    """To square root or no to square."""
    result = [m.sqrt(i) if m.sqrt(i).is_integer() else i**2 for i in arr]
    return result


def count_positives_sum_negatives(arr: list):
    """Count of positives / sum of negatives."""
    if not arr:
        return []

    neg = sum(i for i in arr if i < 0)
    pos = sum(1 for i in arr if i > 0)

    result = [pos, neg]
    return result


def string_to_number(s: int | float):
    """Convert string to number."""
    return int(s)


def am_i_wilson(n: int):
    """Check if number is Wilson prime."""
    if n < 2:
        return False

    return (m.factorial(n - 1) + 1) % n**2 == 0


def two_decimal_places(n: float):
    """Round number to two decimal places."""
    return round(n, 2)


def divisible_by(numbers: list, divisor: int):
    """Filter numbers divisible by divisor."""
    result = [i for i in numbers if i % divisor == 0]
    return result
