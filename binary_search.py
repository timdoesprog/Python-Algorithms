# 29.05.2017
# Implementations of binary search
# O = log n
# array must be sorted

import random


def binary_search(array, value):
    mid = int(len(array) / 2)
    if len(array) == 0:
        return False
    elif array[mid] == value:
        return True
    elif array[mid] < value:
        return binary_search(array[mid + 1:], value)
    elif array[mid] > value:
        return binary_search(array[:mid], value)


def binary_search2(array, value):
    high = len(array) - 1
    low = 0
    while high >= low:
        mid = int((high + low) / 2)
        if array[mid] == value:
            return True
        # go to the left
        elif array[mid] > value:
            high = mid - 1
        # go to the right
        elif array[mid] < value:
            low = mid + 1
    return False


array = [random.randint(1, 200) for x in range(100)]
array.sort()
value = random.randint(1, 200)
print(binary_search2(array, value))
print(array)
print(value)
