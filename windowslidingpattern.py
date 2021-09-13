# import math


# def maxsum_sub_array(arr, k):
#     max_sum = window_sum = window_start = 0
#     for window_end in range(len(arr)):
#         window_sum += arr[window_end]
#         if window_end >= k-1:
#             max_sum = max(max_sum, window_sum)
#             window_sum -= arr[window_start]
#             window_start += 1
#     return max_sum


# print(maxsum_sub_array([2, 3, 4, 5, 6, 7, 8, 9, 10], 2))
# print(maxsum_sub_array([2, 1, 5, 1, 3, 2], 3))


# def minsum_sub_array(arr, k):
#     window_sum = window_start = 0
#     min_length = 10000000000
#     for window_end in range(len(arr)):
#         window_sum += arr[window_end]
#         while window_sum >= k:
#             min_length = min(min_length, window_end - window_start + 1)
#             window_sum -= arr[window_start]
#             window_start += 1
#     if min_length == math.inf:
#         return 0
#     return min_length


# print(minsum_sub_array([2, 1, 5, 2, 3, 2], 7))


def maxitem_sub_array(arr, k):
    window_start = 0
    result = []
    for window_end in range(len(arr)):
        maxItem = max(arr[window_start:window_end+1])
        if window_end >= k-1:
            print("Window ENd STaRT", window_end, window_start)
            print(maxItem)
            result.append(maxItem)
            window_start += 1
    return result


# print(maxitem_sub_array([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
print(maxitem_sub_array([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))
