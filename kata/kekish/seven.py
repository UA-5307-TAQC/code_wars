"""7kuy tasks."""

import math


def divisible_by(numbers, divisor):
    """Find numbers which are divisible by given number."""
    res = []
    for n in numbers:
        if n % divisor == 0:
            res.append(n)
    return res


#     return [if n % divisor == 0 for n in numbers]


def new_avg(arr, new_average):
    """Look for a benefactor."""
    current_sum = 0

    for n in arr:
        current_sum += n

    donation = new_average * (len(arr) + 1) - current_sum

    if donation <= 0:
        raise Exception("")

    return math.ceil(donation)


def series_sum(n):
    """Sum of the first nth term of Series."""
    res = 0
    divisor = 1

    for _ in range(0, n):
        res += 1 / divisor
        divisor += 3

    return f"{res:.2f}"
