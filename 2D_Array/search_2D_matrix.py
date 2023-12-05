## Searching 2D Matrix -------------------------------------------------------------------------------------------------------------





def Searching(mat, target):
    m = len(mat)  # rows
    n = len(mat[0])  # columns

    # Base Case
    if m == 0 or n == 0:
        return -1

    # Binary Search
    low, high = 0, m * n - 1

    while low <= high:
        mid = low + (high - low) // 2
        rowidx = mid // n
        colidx = mid % n

        midelement = mat[rowidx][colidx]

        # Check if the target is equal to the middle element
        if target == midelement:
            return (rowidx, colidx)
        elif target < midelement:
            high = mid - 1
        else:
            low = mid + 1

    return -1

mat = [[1, 3, 5], [7, 10, 11], [16, 20, 23], [30, 34, 60]]
target = 16
result = Searching(mat, target)
print(result)


def Searching(mat, target):
    m = len(mat)  # rows
    n = len(mat[0])  # columns

    # Base Case
    if m == 0 or n == 0:
        return -1

    # Binary Search
    low, high = 0, m * n - 1

    while low <= high:
        mid = low + (high - low) // 2
        rowidx = mid // n
        colidx = mid % n

        midelement = mat[rowidx][colidx]

        # Check if the target is equal to the middle element
        if target == midelement:
            return (rowidx, colidx)
        elif target < midelement:
            high = mid - 1
        else:
            low = mid + 1

    return -1

mat = [[1, 3, 5], [7, 10, 11], [16, 20, 23], [30, 34, 60]]
target = 16
result = Searching(mat, target)
print(result)
