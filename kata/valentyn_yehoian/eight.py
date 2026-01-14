"""Module containing solutions for various 8th kyu katas."""

import math


def litres(time):
    """Calculate litres of water needed based on time in hours."""
    return math.floor(math.floor(time) * 0.5)


def get_volume_of_cuboid(length, width, height):
    """Calculate the volume of a cuboid."""
    return length * width * height


def square_or_square_root(arr):
    """Return square root if integer, otherwise square the number."""
    result = [int(math.sqrt(num)) if math.sqrt(num) == int(math.sqrt(num)) else num * num for num in arr]
    return result


# def square_or_square_root(arr):
#     result = []
#     for num in arr:
#         if math.sqrt(num) == int(math.sqrt(num)):
#             result.append(int(math.sqrt(num)))
#         else:
#             result.append(num * num)
#     return result


def count_positives_sum_negatives(arr):
    """Return count of positive numbers and sum of negative numbers."""
    positive_numbers = 0
    sum_of_negative = 0
    if arr == []:
        return []
    for num in arr:
        if num == 0:
            continue
        if num >= 1:
            positive_numbers += 1
        else:
            sum_of_negative += num
    return [positive_numbers, sum_of_negative]


def string_to_number(s):
    """Convert a string representation of a number to an integer."""
    return int(s)


def am_i_wilson(n):
    """Check if the given number is a Wilson prime."""
    if n < 2 or n > 999:
        return False
    return (math.factorial(n - 1) + 1) % (n * n) == 0


def two_decimal_places(n):
    """Round a number to two decimal places."""
    return round(n, 2)


def divisible_by(numbers, divisor):
    """Return a list of numbers divisible by the given divisor."""
    return [num for num in numbers if (num / divisor).is_integer()]


def converter(mpg):
    """Convert miles per imperial gallon to kilometers per liter."""
    kpl = mpg * (1.609344 / 4.54609188)
    return round(kpl, 2)
