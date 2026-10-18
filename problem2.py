#Problem: Given an array, partition it using the last element as the pivot. Return the pivot's final index after partitioning.

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


arr = [9, 4, 7, 3, 10, 5]
pivot_index = partition(arr, 0, len(arr) - 1)

print("Partitioned array:", arr)
print("Pivot index:", pivot_index)
print("Pivot value:", arr[pivot_index])
