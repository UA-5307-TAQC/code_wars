"""Solutions for 5 kyu tasks."""


def gap(g, m, n):
    """Gap in primes solution."""

    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False

        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    last_prime = None

    for i in range(m, n + 1):
        if is_prime(i):
            if last_prime is not None:
                if i - last_prime == g:
                    return [last_prime, i]

            last_prime = i

    return None


def zeros(n):
    """Number of trailing zeros of N! solution."""
    i = 5
    zero = 0
    while n // i > 0:
        zero += n // i
        i *= 5
    return zero


def perimeter(n):
    """Perimeter of squares in a rectangle solution."""
    a, b = 1, 1
    total_sum = a

    for _ in range(n):
        total_sum += b
        a, b = b, a + b
    return total_sum * 4


def solve(m):
    """Which x for that sum? solution."""
    discriminant_sqrt = (4 * m + 1) ** 0.5
    return (2 * m + 1 - discriminant_sqrt) / (2 * m)


def smallest(n):
    """Find the smallest solution."""
    s = str(n)
    result = [n, 0, 0]

    length = len(s)

    for i in range(length):
        digit = s[i]
        temp_s = s[:i] + s[i + 1 :]

        for j in range(length):
            new_s = temp_s[:j] + digit + temp_s[j:]
            new_n = int(new_s)

            if new_n < result[0]:
                result = [new_n, i, j]

    return result
