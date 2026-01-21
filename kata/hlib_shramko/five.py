"""5kyu tasks."""

from core import kata  # pylint: disable=import-error


@kata("Gap in Primes")
def gap(g, m, n):
    """Gap in Primes."""
    previous = None
    for num in range(m, n + 1):
        if num < 2:
            continue

        is_prime = True
        if num > 2 and num % 2 == 0:
            is_prime = False
        else:
            for i in range(3, int(num**0.5) + 1, 2):
                if num % i == 0:
                    is_prime = False
                    break

        if is_prime:
            if previous is not None and num - previous == g:
                return [previous, num]
            previous = num

    return None


@kata("Number of trailing zeros of N!")
def zeros(n):
    """Number of trailing zeros of N!."""
    count = 0
    i = 5
    while n // i > 0:
        count += n // i
        i *= 5
    return count


@kata("Perimeter of squares in a rectangle")
def perimeter(n):
    """Perimeter of squares in a rectangle."""
    a = b = c = 1
    for _ in range(n):
        c += b
        a, b = b, a + b

    return 4 * c


@kata("Which x for that sum?")
def solve(m):
    """Which x for that sum."""
    return (2 * m + 1 - (4 * m + 1) ** 0.5) / (2 * m)


@kata("Find the smallest")
def smallest(n):
    """Find the smallest."""
    s = str(n)
    best = n
    best_i = best_j = 0

    for i, digit in enumerate(s):
        rest = s[:i] + s[i + 1 :]

        for j in range(len(rest) + 1):
            val = rest[:j] + digit + rest[j:]
            result = int(val)

            if best > result:
                best = result
                best_i = i
                best_j = j

    return [best, best_i, best_j]
