def find_nb(m):
    i = 0
    sum = 0
    while sum < m:
        i += 1
        sum += i ** 3
        if sum == m:
            return i
    return -1
