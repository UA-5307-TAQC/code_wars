"""Solutions for codewars 5kyu"""

import math

from core import kata  # pylint: disable=import-error


def is_prime(value):
    """
    Checks if a number is prime.
    """
    if value == 2:
        return True
    if value % 2 == 0 or value < 2:
        return False
    for i in range(3, int(value**0.5) + 1, 2):
        if value % i == 0:
            return False
    return True


@kata("Gap in Primes")
def gap(g, m, n):
    """
    Finds the first pair of prime numbers between m and n with a gap of g.
    """
    last_prime = None
    for i in range(m, n + 1):
        if is_prime(i):
            if last_prime is not None and i - last_prime == g:
                return [last_prime, i]
            last_prime = i
    return None


@kata("Number of trailing zeros of N!")
def zeros(n):
    """
    Calculates the number of trailing zeros in the factorial of n (n!).
    """
    counter = 0
    while n > 0:
        n = n // 5
        counter += n
    return counter


@kata("Perimeter of squares in a rectangle")
def perimeter(n):
    """
    Calculates the total perimeter of squares arranged in a rectangle.
    """
    a, b = 1, 1
    total_sum = 0

    for _ in range(n + 1):
        total_sum += a
        a, b = b, a + b

    return 4 * total_sum


@kata("Which x for that sum?")
def solve(m):
    """
    Calculates the limit value based on the provided mathematical formula.
    """
    return (2 * m + 1 - math.sqrt(4 * m + 1)) / (2 * m)


@kata("Find the smallest")
def smallest(n):
    """
    Finds the smallest number possible by moving exactly one digit to a new position.
    """
    s = str(n)
    candidates = []

    for i, digit in enumerate(s):
        remaining = s[:i] + s[i + 1 :]

        for j in range(len(s)):
            new_str = remaining[:j] + digit + remaining[j:]
            new_num = int(new_str)
            candidates.append([new_num, i, j])

    return min(candidates)
