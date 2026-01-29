"""
Collection of solutions for 8 kyu Codewars tasks.
"""

import math


def litres(time: float) -> int:
    """
    Calculate how many litres of water are drunk over a given time.

    One litre is drunk every two hours.

    :param time: Time in hours.
    :return: Number of litres consumed.
    """
    time_rounded = math.floor(time)
    consumed_litres = time_rounded // 2
    return consumed_litres


def get_volume_of_cuboid(length: float, width: float, height: float) -> float:
    """
    Calculate the volume of a cuboid.

    :param length: Length of the cuboid.
    :param width: Width of the cuboid.
    :param height: Height of the cuboid.
    :return: Volume of the cuboid.
    """
    return length * width * height


def converter(mpg: float) -> float:
    """
    Convert miles per gallon (MPG) to kilometers per litre (KPL).

    :param mpg: Miles per gallon.
    :return: Kilometers per litre rounded to 2 decimals.
    """
    imperial_gallon_to_litre = 4.54609188
    mile_to_kilometre = 1.609344
    kpl = mpg * (mile_to_kilometre / imperial_gallon_to_litre)
    return round(kpl, 2)


def square_or_square_root(numbers):
    """
       Process numbers by either taking the square root or squaring the number.

       If the square root of a number is an integer, it is added to the result.
       Otherwise, the square of the number is added.

       :param numbers: List of integers.
       :return: Processed list of integers.
       """
    processed_numbers = []

    for number in numbers:
        sqrt_value = math.sqrt(number)
        if sqrt_value.is_integer():
            processed_numbers.append(int(sqrt_value))
        else:
            processed_numbers.append(number**2)

    return processed_numbers


def count_positives_sum_negatives(numbers: list[int]) -> list[int]:
    """
    Count positive numbers and sum negative numbers in a list.

    :param numbers: List of integers.
    :return: List containing count of positives and sum of negatives.
    """
    if not numbers:
        return []

    count_of_positives = 0
    sum_of_negatives = 0

    for number in numbers:
        if number > 0:
            count_of_positives += 1
        elif number < 0:
            sum_of_negatives += number

    return [count_of_positives, sum_of_negatives]


def string_to_number(number_string: str) -> int:
    """
    Convert a string to an integer.

    :param number_string: Numeric string.
    :return: Integer value.
    """
    return int(number_string)


def am_i_wilson(p: int) -> bool:
    """
    Check whether a number is a Wilson prime.

    :param p: Number to check.
    :return: True if Wilson prime, otherwise False.
    """
    if p < 2 or any(p % i == 0 for i in range(2, int(p**0.5) + 1)):
        return False

    return (math.factorial(p - 1) + 1) % (p * p) == 0


def two_decimal_places(num: float) -> float:
    """
    Round a number to two decimal places.

    :param num: Input number.
    :return: Rounded number.
    """
    return round(num, 2)


def divisible_by(numbers: list[int], divisor: int) -> list[int]:
    """
    Return numbers divisible by the given divisor.

    :param numbers: List of integers.
    :param divisor: Divisor.
    :return: List of numbers divisible by divisor.
    """
    return [number for number in numbers if number % divisor == 0]
