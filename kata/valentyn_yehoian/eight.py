import math

def litres(time):
    return math.floor(math.floor(time) * 0.5)

def get_volume_of_cuboid(length, width, height):
   return length * width * height

def square_or_square_root(arr):
    result = [ int(math.sqrt(num)) if math.sqrt(num) == int(math.sqrt(num)) else num*num for num in arr ]
    return result

# def square_or_square_root(arr):
#     result = []
#     for num in arr:
#         if math.sqrt(num) == int(math.sqrt(num)):
#             result.append(int(math.sqrt(num)))
#         else:
#             result.append(num*num)
#     return result

def count_positives_sum_negatives(arr):
    positive_numbers = 0
    sum_of_negative = 0
    if arr == []:
        return []
    for num in arr:
        if num == 0:
            continue
        if num >= 1:
            positive_numbers += 1
        else:
            sum_of_negative += num
    return [positive_numbers, sum_of_negative]

def string_to_number(s):
    return int(s)

def am_i_wilson(n):
    if n < 2 or n > 999:
        return False
    return (math.factorial(n - 1) + 1) % (n * n) == 0

def two_decimal_places(n):
    return round(n,2)


def divisible_by(numbers, divisor):
    return [num for num in numbers if (num / divisor).is_integer()]

def converter(mpg):
    kpl = mpg * (1.609344/4.54609188)
    return round(kpl,2)