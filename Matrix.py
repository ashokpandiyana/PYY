matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def rotateImage(m):
    N = len(m)
    for r in range(N):
        for c in range(r):
            m[r][c], m[c][r] = m[c][r], m[r][c]
    print(m)
    for r in m :
        r.reverse()
    return m


print(rotateImage(matrix))
