"""8kuy tasks."""

import math


def litres(time):
    """Keep Hydrated."""
    return math.floor(time / 2)


def get_volume_of_cuboid(length, width, height):
    """Volume of a Cuboid."""
    return length * width * height


def converter(mpg):
    """Miles per gallon to kilometers per liter."""
    galon_in_liters = 4.54609188
    mile_in_kilometers = 1.609344
    return round(mpg * mile_in_kilometers / galon_in_liters, 2)


def square_or_square_root(arr):
    """To square(root) or not to square(root)."""
    list_of_numbers = []
    for n in arr:
        root = n**0.5
        if root.is_integer():
            list_of_numbers.append(root)
        else:
            list_of_numbers.append(n**2)

    return list_of_numbers  # return [n**(1/2) if n**(1/2).is_integer() else n for n in arr]


def count_positives_sum_negatives(arr):
    """Count of positives / sum of negatives."""
    if arr is None or len(arr) == 0:
        return arr

    positive_count = 0
    negative_sum = 0

    for n in arr:
        if n > 0:
            positive_count += 1
        elif n < 0:
            negative_sum += n

    return [positive_count, negative_sum]


def string_to_number(s):
    """Convert a String to a Number."""
    return int(s)


def is_prime(n):
    """Check if n is prime."""
    if n <= 1:
        return False

    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            return False

    return True


def am_i_wilson(n):
    """Wilson primes."""
    if not is_prime(n):
        return False

    return ((math.factorial(n - 1) + 1) % n**2) == 0


def two_decimal_places(n):
    """Format decimal places."""
    return round(n, 2)


def divisible_by(numbers, divisor):
    """Find numbers which are divisible by given number."""
    res = []
    for n in numbers:
        if n % divisor == 0:
            res.append(n)
    return res  # return [if n % divisor == 0 for n in numbers]
