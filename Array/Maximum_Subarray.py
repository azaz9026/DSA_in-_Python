## Maximum Subarray -------------------------------------------------------------------------------------------------------------------


def MaximumArray(arr):
    sum = 0
    maxi = arr[0]

    for i in range(len(arr)):
        sum += arr[i]

        if sum > maxi:
            maxi = sum

        if sum < 0:
            sum = 0

    return maxi

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = MaximumArray(arr)
print(result)

## Ans -> 6  or [4, -1, 2, 1]
## Time complexit => O(n)

