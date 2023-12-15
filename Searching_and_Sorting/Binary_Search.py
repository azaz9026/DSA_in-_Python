## Binary Search ------------------------------------------------------------------------------------------------------------------------------------------------------


def Binary(arr, target):
    low = 0 
    high = len(arr) - 1  # Fix: subtract 1 to get the correct index

    while low <= high:  # Fix: change the condition to include equality
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [2, 4, 5, 6, 7, 8, 9, 10, 11]  # Fix: ensure the array is sorted
target = 2
result = Binary(arr, target)
print(result)

## Ans -> 0