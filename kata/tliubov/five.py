"""5kyu level tasks."""

from math import sqrt

from core import kata  # pylint: disable=import-error


def is_prime(n):
    """Gap in Primes - find primes."""

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


@kata("Gap in Primes")
def gap(g, m, n):
    """Gap in Primes - find the pair of two prime numbers with a gap."""

    previous_prime = None
    for num in range(m, n + 1):
        if is_prime(num):
            if previous_prime:
                if num - previous_prime == g:
                    return [previous_prime, num]
            previous_prime = num
    return None


@kata("Number of trailing zeros of N!")
def zeros(n):
    """Number of trailing zeros of N."""

    count, i = 0, 1
    while True:
        if not n // 5**i:
            break
        count += n // 5**i
        i += 1
    return count


@kata("Perimeter of squares in a rectangle")
def perimeter(n):
    """Perimeter of squares in a rectangle."""

    sequence = []
    previous_num, next_num = 1, 1
    for _ in range(n + 1):
        sequence.append(previous_num)
        previous_num, next_num = next_num, previous_num + next_num
    perimeter_sum = 4 * sum(sequence)
    return perimeter_sum


@kata("Which x for that sum?")
def solve(m):
    """Find x for the sum."""

    x = 2 * m / (2 * m + 1 + sqrt(4 * m + 1))
    return x


@kata("Find the smallest")
def smallest(n):
    """Find the smallest."""

    smallest_num, num_str = n, str(n)
    from_index = to_index = 0

    for i, digit in enumerate(num_str):
        temp = num_str[:i] + num_str[i + 1 :]

        for j in range(len(temp) + 1):
            value = int(temp[:j] + digit + temp[j:])

            if value < smallest_num or (value == smallest_num and i < from_index):
                smallest_num = value
                from_index, to_index = i, j

    return [smallest_num, from_index, to_index]
