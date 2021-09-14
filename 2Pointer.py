def pairwithsum(arr, k):
    l, r = 0, len(arr)-1
    while(l < r):
        curr_sum = arr[l] + arr[r]
        if k == curr_sum:
            return [l, r]
        if curr_sum > k:
            r -= 1
        else:
            l += 1
    return [-1, -1]


print(pairwithsum([1, 2, 3, 4, 6], 6))
print(pairwithsum([2, 5, 9, 11], 11))


def removeDuplicates(arr):
    next_non_duplicate = 1
    i = 1
    while(i < len(arr)):
        if (arr[i] != arr[next_non_duplicate-1]):
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1
    return next_non_duplicate
