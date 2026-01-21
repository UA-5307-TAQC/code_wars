"""8kyu level tasks."""

from math import factorial, floor, sqrt

from core import kata  # pylint: disable=import-error


@kata("Keep Hydrated!")
def litres(time):
    """Keep Hydrated."""
    return floor(time * 0.5)


@kata("Volume of a Cuboid")
def get_volume_of_cuboid(length, width, height):
    """Volume of a Cuboid."""
    return length * width * height


@kata("Miles per gallon to kilometers per liter")
def converter(mpg):
    """Miles per gallon to kilometers per liter."""
    gallon_to_liters = 4.54609188
    mile_to_km = 1.609344

    kpl = mpg * (mile_to_km / gallon_to_liters)
    return round(kpl, 2)


@kata("To square(root) or not to square(root)")
def square_or_square_root(arr):
    """To square(root) or not to square(root)."""
    squares = []

    for num in arr:
        int_sqrt = floor(sqrt(num))
        if int_sqrt**2 != num:
            squares.append(num**2)
        else:
            squares.append(int_sqrt)

    return squares


@kata("Count of positives / sum of negatives")
def count_positives_sum_negatives(arr):
    """Count of positives / sum of negatives."""
    if not arr:
        return []

    count = 0
    negative_sum = 0

    for num in arr:
        if num > 0:
            count += 1
        else:
            negative_sum += num

    return [count, negative_sum]


@kata("Convert a String to a Number!")
def string_to_number(s):
    """Convert a String to a Number."""
    return int(s)


@kata("Am I Wilson")
def am_i_wilson(n):
    """Wilson primes."""
    if n < 2:
        return False
    return (factorial(n - 1) + 1) % (n**2) == 0


@kata("Formatting decimal places #0")
def two_decimal_places(n):
    """Format decimal places."""
    return round(n, 2)


@kata("Find numbers which are divisible by given number")
def divisible_by(numbers, divisor):
    """Find numbers which are divisible by given number."""
    return [num for num in numbers if not num % divisor]
