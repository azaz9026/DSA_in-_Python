## Sqrt(x)-----------------------------------------------------------------------------------------------------------------


def sqrt(num):
    if num < 2:
        return num

    low = 0
    high = num // 2

    while low <= high:
        mid = low + (high - low) // 2
        mid_squared = mid * mid

        if num < mid_squared:
            high = mid - 1
        elif num > mid_squared:
            low = mid + 1
        else:
            return mid

    return high

num = 25
result = sqrt(num)
print(result)

## Ans -> 2