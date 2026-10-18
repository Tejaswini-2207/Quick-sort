#Problem: Your sorting algorithm frequently receives already sorted arrays. Implement randomized Quick Sort to reduce the likelihood of consistently unbalanced partitions.

import random


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_quick_sort(arr, low, high):
    if low >= high:
        return

    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]

    p = partition(arr, low, high)

    randomized_quick_sort(arr, low, p - 1)
    randomized_quick_sort(arr, p + 1, high)


arr = [1, 2, 3, 4, 5, 6]
randomized_quick_sort(arr, 0, len(arr) - 1)
print(arr)
