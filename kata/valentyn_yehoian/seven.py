"""Module containing solutions for calculating averages and series sums."""

import math

from core import kata  # pylint: disable=import-error


@kata("Looking for a benefactor")
def new_avg(arr, newavg):
    """Calculate the expected donation needed to reach the target average."""
    new_donation = (len(arr) + 1) * newavg - sum(arr)
    if new_donation <= 0:
        raise ValueError("Donation must be positive")
    return math.ceil(new_donation)


@kata("Sum of the first nth term of Series")
def series_sum(n):
    """Calculate the sum of the series 1 + 1/4 + 1/7... up to the nth term."""
    if n == 0:
        return "0.00"
    result = 1
    denominator_offset = 0
    for _ in range(1, n):
        result += 1 / (4 + denominator_offset)
        denominator_offset += 3
    return f"{result:.2f}"
