
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) / 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

        l, r = 0, 0
        for i in range(len(arr)):
            lval = left[l] if l < len(left) else None
            rval = right[r] if r < len(right) else None
            if (lval and rval and lval < rval) or not rval:
                arr[i] = lval
                l += 1
            elif (lval and rval and lval >= rval) or not lval:
                arr[i] = rval
                r += 1
            else:
                pass

if __name__ == '__main__':
    arr = [4, 2, 5, 3, 1, 8]
    merge_sort(arr)
    print(arr)
