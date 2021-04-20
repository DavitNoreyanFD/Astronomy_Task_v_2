"""the quicksort sorting algorithm is used to sort the data, the reason for this is that quicksort is, in most cases,
very optimal in large amounts of data and the complexity is in average O (nlgn). Since my logic we get a matrix of
data and we must sort by a specific column, then our sorting function gets an array and a column index to sort
"""
from random import randint


def quicksort(array, key):
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    pivot = key(array[randint(0, len(array) - 1)])
    for item in array:
        if key(item) > pivot:
            low.append(item)
        elif key(item) == pivot:
            same.append(item)
        elif key(item) < pivot:
            high.append(item)

    return quicksort(low, key) + same + quicksort(high, key)
