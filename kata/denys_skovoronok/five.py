"""File for solving CodeWars 5kyu tasks."""

import math


def gap(g: int, m: int, n: int):
    """Find first prime numbers between m and n that equals g(gap)."""
    prime_list = []

    if not g or not m or not n:
        return None

    for i in range(m, n + 2):

        if len(prime_list) < 2:
            if _is_prime(i):
                prime_list.append(i)

            else:
                continue

        else:
            if prime_list[1] - prime_list[0] == g:
                return prime_list
            prime_list.pop(0)
    return None


def _is_prime(n):
    """Check if n is prime."""
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def zeros(n: int):
    """Find zeroes in factorial of n."""
    result = 0

    while n > 0:
        n = n // 5
        result += n
    return result


def perimeter(n: int):
    """Find perimeter of n integers that raises in fibonacci sequence."""
    if n == 0:
        return 4

    a, b = 1, 1
    total_sum = 2

    for _ in range(n - 1):
        a, b = b, a + b
        total_sum += b

    return total_sum * 4


def solve(m: float):
    """Find x for sum m"""
    return (2 * m + 1 - math.sqrt(4 * m + 1)) / (2 * m)


def smallest(n: int):
    """Find the smallest number, and put it in correct position \
    to get main number the smallest possible."""
    s = str(n)
    digits = list(s)

    best_result = [n, 0, 0]

    for i, digit_to_move in enumerate(digits):
        remaining = digits[:i] + digits[i + 1 :]

        for j in range(len(remaining) + 1):

            current_attempt = remaining[:]
            current_attempt.insert(j, str(digit_to_move))

            num = int("".join(str(x) for x in current_attempt))
            if num < best_result[0]:
                best_result = [num, i, j]
    return best_result
