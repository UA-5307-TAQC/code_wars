"""7 kyu tasks"""

import math


def new_avg(arr, newavg):
    """Looking for a benefactor."""
    sum_dobations = sum(arr)
    len_donations = len(arr)

    needed_total = newavg * (len_donations + 1)

    new_don = needed_total - sum_dobations

    if new_don <= 0:
        raise ValueError

    return math.ceil(new_don)


def series_sum(n):
    """Sum of the first nth term of Series."""
    total = 0

    for i in range(1, n + 1):
        znamenyk = 1 + (i - 1) * 3
        total += 1 / znamenyk

    return "{:.2f}".format(total)