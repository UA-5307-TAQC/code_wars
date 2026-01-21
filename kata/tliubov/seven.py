"""7kyu level tasks."""


def new_avg(arr, newavg):
    """Look for a benefactor."""
    x = newavg * (len(arr) + 1) - sum(arr)
    if x <= 0:
        raise ValueError("The last donation is a non positive number")
    return x


def series_sum(n):
    """Sum of the first nth term of Series."""
    total = 0
    for num in range(1, n + 1):
        total += 1 / (3 * num - 2)
    return f"{total:.2f}"
