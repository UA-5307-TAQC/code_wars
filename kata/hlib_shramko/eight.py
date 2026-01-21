"""8kyu tasks."""

from core import Tasks, kata  # pylint: disable=import-error


@kata(Tasks.EIGHT.value.litres)
def litres(time):
    """Keep Hydrated."""
    return int(time * 0.5)


@kata("Volume of a Cuboid")
def get_volume_of_cuboid(length, width, height):
    """Volume of a Cuboid."""
    return length * width * height


@kata("Miles per gallon to kilometers per liter")
def converter(mpg):
    """Miles per gallon to kilometers per liter."""
    return round(mpg / 4.54609188 * 1.609344, 2)


@kata("To square(root) or not to square(root)")
def square_or_square_root(arr):
    """To square(root) or not to square(root)."""
    result = []
    for i in arr:
        if int(i**0.5) ** 2 == i:
            result.append(int(i**0.5))
        else:
            result.append(int(i**2))
    return result


@kata("Count of positives / sum of negatives")
def count_positives_sum_negatives(arr):
    """Count of positives / sum of negatives."""
    count_pos = 0
    sum_neg = 0

    if not arr:
        return []

    for i in arr:
        if i > 0:
            count_pos += 1
        elif i < 0:
            sum_neg += i

    if not arr:
        return []

    return [count_pos, sum_neg]


@kata("Convert a String to a Number!")
def string_to_number(s):
    """Convert a String to a Number."""
    return int(s)


@kata("Am I Wilson")
def am_i_wilson(n):
    """Wilson primes."""
    if n < 2:
        return False

    fact = 1
    for i in range(1, n):
        fact *= i

    return (fact + 1) % (n * n) == 0


@kata("Formatting decimal places #0")
def two_decimal_places(n):
    """Format a number to n decimal places."""
    return round(n, 2)


@kata("Find numbers which are divisible by given number")
def divisible_by(numbers, divisor):
    """Find numbers which are divisible by given number."""
    result = []
    for i in numbers:
        if i % divisor == 0:
            result.append(i)

    return result
