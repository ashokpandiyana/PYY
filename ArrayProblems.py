# # remove-duplicates-from-sorted-array
# def removeDuplicates(A):
#     if not A:
#         return 0

#     last = 0
#     for i in range(1, len(A)):
#         if A[last] != A[i]:
#             last += 1
#             A[last] = A[i]
#     return last + 1


# # print(removeDuplicates([1, 1, 2, 3, 4, 4]))


# def removeElement(A, elem):
#     i, last = 0, len(A) - 1
#     while i <= last:
#         if A[i] == elem:
#             A[i], A[last] = A[last], A[i]
#             last -= 1
#         else:
#             i += 1
#     print(A)
#     return last + 1


# print(removeElement([1, 2, 3, 4, 3, 2], 3))

def firstMissingPositive(nums):
    if nums == []:
        return 1
    if nums == [1]:
        return 2
    leng = len(nums) + 1
    for i in range(1, leng+1):
        if i not in nums:
            return i


print(firstMissingPositive([3, 4, -1, 1]))
