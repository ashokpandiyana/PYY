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

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        cvalue = A[i]
        position = i
        while position > 0 and A[position-1] > cvalue:
            A[position] = A[position-1]
            position = position - 1
        A[position] = cvalue
    return A


print(insertionSort([4, 7, 2, 3, 10, 1, 5]))
