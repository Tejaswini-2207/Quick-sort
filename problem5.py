#Problem: Sort only the elements between indices 1 and 4, inclusive. Keep all other positions unchanged.

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


arr = [90, 8, 3, 7, 1, 60]

left = 1
right = 4

quick_sort(arr, left, right)

print(arr)
