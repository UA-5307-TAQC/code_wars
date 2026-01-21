"""File for solving CodeWars 7kyu tasks."""

import math


def new_avg(arr: list, newavg: int):
    """Calculate the expected donation."""
    sum_of_array = sum(i for i in arr)
    expected_number = (newavg * (len(arr) + 1)) - sum_of_array

    if math.ceil(expected_number) < newavg:
        return 1 / 0
    return math.ceil(expected_number)


def series_sum(n: int):
    """Calculate the first nth term of the series."""
    if n == 0:
        return "0.00"
    if n == 1:
        return "1.00"

    result = 1
    denominator = 1
    for _ in range(1, n):
        denominator += 3
        result += 1 / denominator

    return format(result, ".2f")
