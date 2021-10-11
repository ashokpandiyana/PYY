# def selectionSort(a):
#     n = len(a)
#     for i in range(n-1):
#         position = i
#         for j in range(i+1, n):
#             if a[j] < a[position]:
#                 position = j
#         a[i], a[position] = a[position], a[i]
#     return a


# print(selectionSort([4, 7, 2, 3, 10, 1, 5]))

# def insertionSort(A):
#     n = len(A)
#     for i in range(1, n):
#         cvalue = A[i]
#         position = i
#         while position > 0 and A[position-1] > cvalue:
#             A[position] = A[position-1]
#             position = position - 1
#         A[position] = cvalue
#     return A


# print(insertionSort([4, 7, 2, 3, 10, 1, 5]))


# def bubbleSort(A):
#     n = len(A)
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if A[i] > A[j]:
#                 A[i], A[j] = A[j], A[i]
#     return A


# print(bubbleSort([1, 3, 2, 4, 6, 9, 8 ]))

# def shellSort(A):
#     n = len(A)
#     gap = n // 2
#     while gap > 0:
#         i = gap
#         while i < n:
#             temp = A[i]
#             j = i-gap
#             while j >= 0 and A[j] > temp:
#                 A[j+gap] = A[j]
#                 j = j-gap
#             A[j+gap] = temp
#             i = i + 1
#         gap = gap // 2
#     return A


# print(shellSort([1, 5, 4, 7, 8, 9, 3, 2]))
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


arr = [12, 11, 13, 5, 6, 7]
print("Given array is", end="\n")
printList(arr)
mergeSort(arr)
print("Sorted array is: ", end="\n")
printList(arr)
