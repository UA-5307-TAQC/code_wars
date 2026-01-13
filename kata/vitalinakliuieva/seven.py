import math

#Looking for a benefactor exercise
def new_avg(arr, newavg):
    needed = newavg * (len(arr) + 1) - sum(arr)
    needed = math.ceil(needed)
    if needed <= 0:
        raise ValueError("Expected donation must be a positive number")
    return needed

#Sum of the first nth term of Series exercise
def series_sum(n):
    if n == 0:
        return "0.00"

    total = 0.0
    denominator = 1

    for _ in range(n):
        total += 1 / denominator
        denominator += 3

    return f"{total:.2f}"

