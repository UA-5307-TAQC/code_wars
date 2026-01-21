"""Solutions for 7 kyu tasks"""

import math

from core import kata  # pylint: disable=import-error


@kata("Looking for a benefactor")
def new_avg(arr, newavg):
    """Looking for a benefactor."""
    sum_of_donations = sum(arr)
    next_donation = newavg * (len(arr) + 1) - sum_of_donations
    if next_donation <= 0:
        raise ValueError

    return math.ceil(next_donation)


@kata("Sum of the first nth term of Series")
def series_sum(n):
    """Sum of the first nth term of Series."""
    result = sum(1 / (1 + 3 * i) for i in range(n))

    return f"{result:.2f}"
