import math

#Keep Hydrated! exercise
def litres(time):
    litrescount = math.floor(time/2)
    return litrescount

#Volume of a Cuboid exercise
def get_volume_of_cuboid(length, width, height):
    volume = length * width * height
    return volume

#Miles per gallon to kilometers per liter exercise
def converter(mpg):
    klp = round((mpg * 1.609344)/4.54609188, 2)
    return klp

#To square(root) or not to square(root) exercise
def square_or_square_root(arr):
    resultarr = []
    for num in arr:
        if (math.sqrt(num)).is_integer():
            resultarr.append(int(math.sqrt(num)))
        else:
            resultarr.append(num**2)
    return resultarr

#Count of positives / sum of negatives exercise
def count_positives_sum_negatives(arr):
    resultarr = []
    negative = 0
    positive = 0
    if arr:
        for num in arr:
            if num>0 :
                positive += 1
            elif num<0:
                negative += num
        resultarr.append(positive)
        resultarr.append(negative)
    return resultarr

#Convert a String to a Number! exercise
def string_to_number(s):
    return int(s)

#Wilson primes exercise
def am_i_wilson(n):
    if n <= 1:
        return False

    return ((math.factorial(n - 1) + 1) / (n * n)).is_integer()

#Formatting decimal places exercise
def two_decimal_places(n):
    return round(n, 2)

#Find numbers which are divisible by given number exercise
def divisible_by(numbers, divisor):
    resultarr = []
    for num in numbers:
        if num%divisor == 0:
            resultarr.append(num)
    return resultarr


