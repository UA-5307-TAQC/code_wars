"""5kyu tasks."""

from math import sqrt


def gap(g, m, n):
    """Gap in Primes - find primes."""
    prev = None

    for x in range(m, n + 1):
        if x < 2:
            continue

        is_prime = True
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                is_prime = False
                break

        if is_prime:
            if prev is not None and x - prev == g:
                return [prev, x]
            prev = x

    return None


def zeros(n):
    """Number of trailing zeros of N."""
    count = 0
    while n >= 5:
        n = n // 5
        count += n
    return count


def perimeter(n):
    """Perimeter of squares in a rectangle."""
    n0 = 1
    n1 = 1
    sum_of_sides = 0

    for _ in range(n + 1):
        sum_of_sides += n0
        next_value = n0 + n1
        n0 = n1
        n1 = next_value

    return sum_of_sides * 4


def solve(m):
    """Which x for that sum?"""
    disc = (2 * m + 1) ** 2 - 4 * m * m
    x = ((2 * m + 1) - sqrt(disc)) / (2 * m)
    return x


def smallest(n):
    """Find the smallest."""
    s = str(n)
    best = (n, 0, 0)

    for i, digit in enumerate(s):
        rest = s[:i] + s[i + 1 :]

        for j in range(len(rest) + 1):
            candidate = rest[:j] + digit + rest[j:]
            candidate_num = int(candidate)
            best = min(best, (candidate_num, i, j))

    return list(best)
