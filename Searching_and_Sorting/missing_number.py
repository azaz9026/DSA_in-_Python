## missing number --------------------------------------------------------------------------------------------------------------------------------------------

def find_missing_number(arr):
    n = len(arr) + 1  # One number is missing, so array length + 1 is the expected length
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    return missing_number

# Example usage:
arr = [1, 2, 4, 6, 3, 7, 8]
result = find_missing_number(arr)
print(result)


## another method --------------------------------------------------------------------------------------------------------------------------------------------------------


def find_missing_number(arr):
    n = len(arr) + 1  # One number is missing, so array length + 1 is the expected length
    actual = 0
    expected = n*(n+1)//2
    for num in arr:
        actual += num

    missing_number = expected - actual
    return missing_number

# Example usage:
arr = [1, 2, 4, 6, 3, 7, 8]
result = find_missing_number(arr)
print(result)




## another method --------------------------------------------------------------------------------------------------------------------------------------------------------


def find_missing_number(arr):
    sorted_arr = sorted(arr)  # Use sorted() to create a sorted copy
    missing_number = len(sorted_arr)

    for i, num in enumerate(sorted_arr):
        missing_number ^= i ^ num

    return missing_number

# Example usage:
arr = [1, 2, 4, 6, 3, 7, 8]
result = find_missing_number(arr)
print(result)




## another method --------------------------------------------------------------------------------------------------------------------------------------------------------




def find_missing_number_sorted(arr):
    n = len(arr)
    
    for i in range(1, n):
        if arr[i] != arr[i - 1] + 1:
            return arr[i - 1] + 1

    # If no missing number found in the loop, the missing number is at the end
    return arr[-1] + 1

# Example usage:
arr = [1, 2, 3, 4, 6, 7, 8]
result = find_missing_number_sorted(arr)
print(result)
