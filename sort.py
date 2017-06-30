# 24.02.2017
# Implement different sort algorithms

import random

# 1. Bubble sort
#   highest numbers bubble to the end of list
# O(n**n)


# uses two nested loops
def bubblesort(array):
    for i in range(0, len(array) - 1):
        for j in range(0, len(array) - 1 - i):
            # if the left item array[j] is bigger than the right
            # item array[j+1] then we swap them
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


# 2. MergeSort
# divide an conquer algorithm
# O(n logn)
# Source: http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html
# edited for better readability

def mergeSort(array):
    print(array)
    print()
    # if array is of size 1 it is already sorted, so nothing needs to be done
    if len(array) > 1:
        # split the array into two smaller parts // divide and conquer
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        # recursive call on both halves
        mergeSort(left_half)
        mergeSort(right_half)

        # merge part
        i = 0
        j = 0
        k = 0
        # two finger algorithm
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        # append the rest to the array if there is any left
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
        print(array)
        print()


array = [random.randint(1, 100) for i in range(10)]
print(array)
mergeSort(array)
print(array)

# bubblesort(array)
# print(array)
