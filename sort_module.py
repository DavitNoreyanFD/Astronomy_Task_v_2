"""the quicksort sorting algorithm is used to sort the data, the reason for this is that quicksort is, in most cases,
very optimal in large amounts of data and the complexity is in average O (nlgn). Since my logic we get a matrix of
data and we must sort by a specific column, then our sorting function gets an array and a column index to sort
"""
from random import randint


def quicksort(array: list, key) -> list:
    if len(array) < 2:
        return array
    left, same, right = [], [], []
    pivot = key(array[randint(0, len(array) - 1)])
    for item in array:
        if key(item) > pivot:
            left.append(item)
        elif key(item) == pivot:
            same.append(item)
        elif key(item) < pivot:
            right.append(item)

    return quicksort(left, key) + same + quicksort(right, key)
