import math

def new_avg(arr, newavg):
    new_donation = (len(arr) + 1) * newavg - sum(arr)
    if new_donation <= 0:
        raise ValueError("Donation must be positive")
    return math.ceil(new_donation)

def series_sum(n):
    if n == 0:
        return "0.00"
    result = 1
    state = 0
    i = 1
    while i < n:
        i+=1
        result += 1/(4+state)
        state += 3
    return f"{result:.2f}"