vertices = 5
A = [[0 for column in range(vertices)]
     for row in range(vertices)]
print(A)

# Transpose
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[0 for column in range(len(A))]
     for row in range(len(A[0]))]
for i in range(len(A)):
    for j in range(len(A[0])):
        B[j][i] = A[i][j]
print(B)
