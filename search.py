# 10.02.2017
# create a binary search algorithm and test against linear search
# List size: 100 000 from 0 to 99 999
# Target: random number inside the list
# Binary Search: 0.0119s
# Linear Seatch: 4.0744s


from timeit import default_timer as timer
import random

# get a list of numbers from 0 - 1000
numbers = [i for i in range(100000)]

def find_binary(target, array):
    # initialize two pointers to the start and end of the list
    low = 0
    high = len(array) - 1
    while low <= high:
        # get the current middle of the remaining list
        mid = int((low + high) / 2)
        # check if the target is at the current middle
        if array[mid] == target:
            return True
        # otherwise adjust the middle accordingly
        elif array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
    # after the list has been search and the target wasn't found
    return False

def find_linear(target, array):
    for i in range(0, len(array)):
        if array[i] == target:
            return True
    return False


# time both functions with 1000 repetitions
start = timer()
for i in range(1000):
    target = random.randint(0, 99999)
    find_binary(target, numbers)
end = timer()
print("Binary Search: {}s".format(end - start))

start = timer()
for i in range(1000):
    target = random.randint(0, 99999)
    find_linear(target, numbers)
end = timer()
print("Linear Search: {}s".format(end - start))
