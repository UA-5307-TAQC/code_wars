"""Solutions for Codewars kata (5 kyu)."""

import math

from core import kata  # pylint: disable=import-error


@kata("Gap in Primes")
def gap(g, m, n):
    """Gap in Primes exercise"""
    last_prime = None
    for num in range(m, n + 1):
        if is_prime(num):
            if last_prime is not None and num - last_prime == g:
                return [last_prime, num]
            last_prime = num
    return None


def is_prime(n):
    """Check if number is prime."""
    # Це допоміжна функція, тому декоратор зазвичай не потрібен,
    # якщо тільки це не окрема задача (наприклад, 'Is a number prime?')
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))


@kata("Number of trailing zeros of N!")
def zeros(n):
    """Number of trailing zeros of N! exercise"""
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count


@kata("Perimeter of squares in a rectangle")
def perimeter(n):
    """Perimeter of squares in a rectangle"""
    previous = 1
    second_var = 1
    total = 1
    for _ in range(n):
        previous, second_var = second_var, previous + second_var
        total += previous
    return 4 * total


@kata("Which x for that sum?")
def solve(m):
    """Which x for that sum?"""
    return (2 * m + 1 - math.sqrt(4 * m + 1)) / (2 * m)


@kata("Find the smallest")
def smallest(n):
    """Find the smallest"""
    num = str(n)
    best = (n, 0, 0)

    for i, _ in range(len(num)):
        digit = num[i]
        rest = num[:i] + num[i + 1 :]

        for j in range(len(rest) + 1):
            candidate = int(rest[:j] + digit + rest[j:])
            if candidate < best[0]:
                best = (candidate, i, j)

    return list(best)
