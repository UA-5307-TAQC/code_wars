"""Module containing solutions for calculating averages and series sums."""

import math


def new_avg(arr, newavg):
    """Calculate the expected donation needed to reach the target average."""
    new_donation = (len(arr) + 1) * newavg - sum(arr)
    if new_donation <= 0:
        raise ValueError("Donation must be positive")
    return math.ceil(new_donation)


def series_sum(n):
    """Calculate the sum of the series 1 + 1/4 + 1/7... up to the nth term."""
    if n == 0:
        return "0.00"
    result = 1
    state = 0
    i = 1
    while i < n:
        i += 1
        result += 1 / (4 + state)
        state += 3
    return f"{result:.2f}"
