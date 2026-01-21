"""Solutions for 7 kyu tasks."""


def new_avg(arr: list, newavg):
    """Look for a benefactor solution."""
    actual_sum = sum(arr)
    res = (len(arr) + 1) * newavg - actual_sum
    if res > 0:
        return res if res % 1 == 0 else int(res) + 1
    raise ValueError


def series_sum(n):
    """Sum of the first nth term of series solution."""
    res = 0
    last_from_sequence = 1 + 3 * (n - 1)
    for i in range(1, last_from_sequence + 1, 3):
        res += 1 / i
    return f"{res:.2f}"
