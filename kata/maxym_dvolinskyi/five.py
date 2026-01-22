"""Solutions for 8 kyu tasks"""


def gap(g, m, n):
    """Gap in Primes."""

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    last_prime = None
    start = m if m % 2 != 0 else m + 1

    for i in range(start, n + 1, 2):
        if is_prime(i):
            if last_prime is not None and i - last_prime == g:
                return [last_prime, i]
            last_prime = i

    return None


def zeros(n):
    """Number of trailing zeros of N!."""
    count = 0

    while n > 0:
        n //= 5
        count += n

    return count


def perimeter(n):
    """Perimeter of squares in a rectangle."""
    a, b = 1, 1
    sum_ = 0

    for _ in range(n + 1):
        sum_ += a
        a, b = b, a + b

    return 4 * sum_


def solve(m):
    """Which x for that sum."""
    delta = (4 * m + 1) ** (0.5)
    x = (2 * m + 1 - delta) / (2 * m)

    return x


def smallest(n):
    """Find the smallest."""
    s = str(n)
    min_res = [n, 0, 0]

    for i, digit in enumerate(s):
        temp_s = s[:i] + s[i + 1 :]

        for j in range(len(s)):

            new_s = temp_s[:j] + digit + temp_s[j:]
            new_n = int(new_s)

            if new_n < min_res[0]:
                min_res = [new_n, i, j]

    return min_res
