#problem: Find the \(k\)-th smallest element without completely sorting the array.

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def kth_smallest(arr, k):
    if not 1 <= k <= len(arr):
        raise ValueError("k must be between 1 and array length")

    low, high = 0, len(arr) - 1
    target = k - 1

    while low <= high:
        p = partition(arr, low, high)

        if p == target:
            return arr[p]
        elif p < target:
            low = p + 1
        else:
            high = p - 1


arr = [12, 3, 5, 7, 19, 1]
k = 3

print(kth_smallest(arr, k))
