def selectionSort(a):
    n = len(a)
    for i in range(n-1):
        position = i
        for j in range(i+1, n):
            if a[j] < a[position]:
                position = j
        a[i], a[position] = a[position], a[i]
    return a


print(selectionSort([4, 7, 2, 3, 10, 1, 5]))
