import math
import numpy as np

def ex1_hydration(time):
    time_rounded = math.floor(time)
    litres = int(time_rounded / 2)
    return litres

def ex2_volume(length, width, height):
    volume = length * width * height
    return volume

def ex3_mpg_to_kpl(mpg):
    ig_to_litre = 4.54609188
    mile_to_kilometre = 1.609344
    mpg_to_kpl = mile_to_kilometre / ig_to_litre
    kpl = mpg * mpg_to_kpl
    kpl_rounded = round(kpl, 2)
    return kpl_rounded

def ex4_square(numbers):
    processed_numbers = []
    for num in numbers:
        sqrt_num = math.sqrt(num)
        square_num = math.pow(num, 2)
        if sqrt_num.is_integer():
            processed_numbers.append(int(sqrt_num))
        else:
            processed_numbers.append(int(square_num))
    return processed_numbers

def ex5_count_and_sum(numbers):
    count_of_positives = 0
    sum_of_negatives = 0
    result = []
    if not numbers:
        return result
    for num in numbers:
        if num > 0:
            count_of_positives += 1
        elif num < 0:
            sum_of_negatives += num
    result.append(count_of_positives)
    result.append(sum_of_negatives)
    return result

def ex6_convert(number_string):
    number_int = int(number_string)
    return number_int

def ex7_wilson_primes(p):
    if p < 2 or any(p % i == 0 for i in range(2, int(p**0.5) + 1)):
        return False
    return (math.factorial(p - 1) + 1) % (p * p) == 0

def ex8_decimal_places(num):
    num_rounded = round(num, 2)
    return num_rounded

def ex9_divisible_numbers(numbers, divisor):
    processed_numbers = []
    for num in numbers:
        if num % divisor == 0:
            processed_numbers.append(int(num))
    return processed_numbers