"""5kuy tasks."""

import math

from core import kata  # pylint: disable=import-error


def is_prime(n):
    """Check if n is prime."""
    if n <= 1:
        return False

    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            return False

    return True


@kata("Gap in Primes")
def gap(g, m, n):
    """Find gap between two prime numbers."""
    previous_prime = None

    for x in range(m, n + 1):
        if not is_prime(x):
            continue

        if previous_prime is None:
            previous_prime = x
            continue

        if x - previous_prime == g:
            return [previous_prime, x]

        previous_prime = x
    return None


@kata("Number of trailing zeros of N!")
def zeros(n):
    """Number of trailing zeros of N."""
    if n < 0:
        return 0

    count = 0
    power_of_5 = 5

    while power_of_5 <= n:
        count += n // power_of_5
        power_of_5 *= 5

    return count


@kata("Perimeter of squares in a rectangle")
def perimeter(n):
    """Find perimeter of squares in a rectangle."""
    a, b = 1, 1
    for _ in range(n + 2):
        a, b = b, a + b
    return 4 * (a - 1)


@kata("Which x for that sum?")
def solve(m):
    """Which x for that sum."""
    b = -(2 * m + 1)

    discriminant = b**2 - 4 * m**2
    sqrt_d = math.sqrt(discriminant)

    x1 = (-b - sqrt_d) / (2 * m)
    x2 = (-b + sqrt_d) / (2 * m)

    if 0 < x1 < 1:
        return x1
    return x2


@kata("Find the smallest")
def smallest(n):
    """Find smallest number in a sequence."""
    digits = str(n)
    length = len(digits)

    best = (n, 0, 0)

    for i in range(length):
        digit = digits[i]
        remaining = digits[:i] + digits[i + 1 :]

        for j in range(length):
            candidate = remaining[:j] + digit + remaining[j:]
            value = int(candidate)

            result = (value, i, j)
            best = min(best, result)

    return list(best)
