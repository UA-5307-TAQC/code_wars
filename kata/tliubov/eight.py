from math import floor, sqrt, factorial

# 1.Keep Hydrated!
def litres(time):
    return floor(time * 0.5)


# 2.Volume of a Cuboid
def get_volume_of_cuboid(length, width, height):
    return length * width * height


# 3.Miles per gallon to kilometers per liter
def converter(mpg):
    gallon_to_liters = 4.54609188
    mile_to_km = 1.609344
    
    kpl = mpg * (mile_to_km/gallon_to_liters)
    return round(kpl, 2)   


# 4.To square(root) or not to square(root)
def square_or_square_root(arr):
    squares = []
    
    for num in arr:
        int_sqrt = floor(sqrt(num))
        if int_sqrt**2 != num:
            squares.append(num**2)
        else:
            squares.append(int_sqrt)
        
    return squares


# 5.Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    
    count = 0
    sum = 0
    
    for num in arr:
        if num > 0:
            count += 1
        else:
            sum += num
        
    return [count, sum]


# 6.Convert a String to a Number
def string_to_number(s):
    return int(s)


# 7.Wilson primes
def am_i_wilson(n):
    if n < 2:
        return False
    
    numerator = factorial(n-1) + 1
    result = numerator / n**2
    if floor(result) == result:
        return True
    return False


# 8.Formatting decimal places
def two_decimal_places(n):
    return round(n, 2)


# 9.Find numbers which are divisible by given number
def divisible_by(numbers, divisor):
    return [num for num in numbers if num % divisor == 0]

