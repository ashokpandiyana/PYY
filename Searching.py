def linearSearch(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i+1
    return -1


def binarySearch(arr, k):
    l, r = 0, len(arr)-1
    while l < r:
        mid = l + r // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            r = mid
        else:
            l = mid
    return -1


print(linearSearch([1, 2, 5, 4, 7, 6, 8], 5))
print(binarySearch([1, 2, 3, 4, 5, 6, 7], 2))
