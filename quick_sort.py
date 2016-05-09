
def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i


def quick_sort_helper(arr, lo, hi):
    if lo < hi:
        i = partition(arr, lo, hi)
        quick_sort_helper(arr, lo, i - 1)
        quick_sort_helper(arr, i + 1, hi)


def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    arr = [4, 2, 5, 3, 1, 8]
    quick_sort(arr)
    print(arr)
