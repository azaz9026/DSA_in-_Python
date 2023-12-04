
## Transpose Matrix -----------------------------------------------------------------------------------------

def Transpose(mat):
    m = len(mat)
    n = len(mat[0])

    # Create a new matrix using list comprehension
    result = [[mat[j][i] for j in range(m)] for i in range(n)]

    return result

met = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = Transpose(met)
print(res)



## Second method


def Transpose(mat):
    m = len(mat)
    n = len(mat[0])

    # Create a new matrix filled with zeros
    result = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(0, n):
        for j in range(0, m):
            result[i][j] = mat[j][i]

    return result

met = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = Transpose(met)
print(res)