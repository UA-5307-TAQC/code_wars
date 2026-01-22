import math
import numpy as np

def new_avg(donations, average):
    donations_sum = 0
    donations_count = 0
    for donation in donations:
        donations_sum += int(donation)
        donations_count += 1
    donations_count += 1
    expected_sum = average * donations_count
    expected_donation = expected_sum - donations_sum
    if expected_donation < 0:
        return "ERROR"
    return expected_donation

def series_sum(n):
    if n == 0:
        return "\"0.00\""
    series = [1 / (3 * i - 2) for i in range(1, n + 1)]
    series_sum = sum(series)
    series_sum_rounded = round(series_sum, 2)
    return f"\"{series_sum_rounded}\""