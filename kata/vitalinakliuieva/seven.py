"""Solutions for Codewars kata (7 kyu)."""
import math

def new_avg(arr, new_num):
    """Looking for a benefactor exercise"""
    needed = new_num * (len(arr) + 1) - sum(arr)
    needed = math.ceil(needed)
    if needed <= 0:
        raise ValueError("Expected donation must be a positive number")
    return needed


def series_sum(n):
    """Sum of the first nth term of Series exercise"""
    if n == 0:
        return "0.00"

    total = 0.0
    denominator = 1

    for _ in range(n):
        total += 1 / denominator
        denominator += 3

    return f"{total:.2f}"

