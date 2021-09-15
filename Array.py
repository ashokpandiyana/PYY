def reverse(a):
    l, r = 0, len(a)-1
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1
    return a


def minmax(a):
    min_value = 1000000
    max_value = 0
    for i in a:
        if i < min_value:
            min_value = i
        if i > max_value:
            max_value = i
    return [min_value, max_value]


def sort012(a):
    lo = 0
    hi = len(a) - 1
    mid = 0
    while mid <= hi:
        if a[mid] == 0:
            a[lo], a[mid] = a[mid], a[lo]
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        else:
            a[mid], a[hi] = a[hi], a[mid]
            hi = hi - 1
    return a


def rearrange(a):
    j = 0
    for i in range(len(a)):
        if a[i] < 0:
            a[i], a[j] = a[j], a[i]
            j += 1
    return a


def printUnion(arr1, arr2, n1, n2):
    hs = set()
    for i in range(0, n1):
        hs.add(arr1[i])
    for i in range(0, n2):
        hs.add(arr2[i])
    print("Union:")
    for i in hs:
        print(i, end=" ")
    print("\n")


def printIntersection(arr1, arr2, n1, n2):
    hs = set()
    for i in range(0, n1):
        hs.add(arr1[i])
    print("Intersection:")
    for i in range(0, n2):
        if arr2[i] in hs:
            print(arr2[i], end=" ")

# Kadane Algorithm


def largestSum(arr):
    sum_value = max_value = arr[0]
    for i in range(1, len(arr)):
        sum_value = max(arr[i], sum_value+arr[i])
        max_value = max(max_value, sum_value)
    return max_value


arr1 = [7, 1, 5, 2, 3, 6]
arr2 = [3, 8, 6, 20, 7]
n1 = len(arr1)
n2 = len(arr2)
print(reverse([1, 2, 3, 4, 5]))
print(minmax([1, 2, 3, 4, 5]))
print(sort012([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))
print(rearrange([-1, 2, -3, 4, 5, 6, -7, 8, 9]))
# printUnion(arr1, arr2, n1, n2)
# printIntersection(arr1, arr2, n1, n2)
print(largestSum([-2, -3, 4, -1, -2, 1, 5, -3]))
