## Sum Diagonal -------------------------------------------------------------------------------------------------------------


def SumDiagonal(mat):
    n = len(mat)
    result = 0

    for i in range(0, n):
        ## primary diagonal
        result += mat[i][i]
        ## second diagonal 
        result += mat[n - i - 1][i]

    ## n is Odd
    if n % 2 == 0:
        return result
    else:
        result -= mat[n // 2][n // 2]
        return result

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Sum = SumDiagonal(mat)
print(Sum)


## Ans => 25
## Time complexit => O(n)