"""7kyu tasks."""

import math

from core import kata  # pylint: disable=import-errorі


@kata("Looking for a benefactor")
def new_avg(arr, newavg):
    """Calculate the next donation needed to reach a target average."""
    n = len(arr)
    sum_arr = sum(arr)
    result = math.ceil(newavg * (n + 1) - sum_arr)

    if result <= 0:
        raise ValueError

    return result


@kata("Sum of the first nth term of Series")
def series_sum(n):
    """Sum of the first nth term of Series."""
    result = 0
    for i in range(1, n + 1):
        result += 1 / (3 * i - 2)

    return f"{result:.2f}"
