import math
import numpy as np

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def ex18_gap(g, m, n):
    prev = None
    for i in range(m, n + 1):
        if is_prime(i):
            if prev is not None and i - prev == g:
                return [prev, i]
            prev = i
    return None

def ex19_trailing_zeros(n):
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count

def ex20_squares(count):
    perimeter = 0
    previous_square = 0
    current_square = 1
    for i in range(count+1):
        perimeter += current_square * 4
        new_square = previous_square + current_square
        previous_square = current_square
        current_square = new_square
    return perimeter

def ex21_find_x(m):
    b = ((-2) * m) - 1
    discriminant = math.pow(b, 2) - 4 * m * m
    x_1 = (math.sqrt(discriminant) - b) / (2 * m)
    x_2 = (0 - b - math.sqrt(discriminant)) / (2 * m)
    if 0 < x_1 < 1:
        return x_1
    elif 0 < x_2 < 1:
        return x_2
    else:
        return "The desired x does not exist"

def ex22_smallest(number):
    numbers = []
    indexes_took = []
    indexes_insert = []
    s_num = str(number)
    for i in range(len(s_num)):
        for j in range(len(s_num)):
            digit_to_move = s_num[i]
            temp_s_num = s_num[:i] + s_num[i+1:]
            new_s_num = temp_s_num[:j] + digit_to_move + temp_s_num[j:]
            new_number = int(new_s_num)
            numbers.append(new_number)
            indexes_took.append(i)
            indexes_insert.append(j)
    min_number = min(numbers)
    min_index = numbers.index(min_number)
    return [min_number, indexes_took[min_index], indexes_insert[min_index]]