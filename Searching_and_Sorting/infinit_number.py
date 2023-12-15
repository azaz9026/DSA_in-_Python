## find the first occurrence of the positive infinity


arr = [2, 4,  5, float('inf') , 7, 9, 6, 10, 11]

def find_first_infinity(arr):
    for i in range(len(arr)):
        if arr[i] == float('inf'):
            return i
    return -1  # Return -1 if no infinity is found

result = find_first_infinity(arr)
print(result)


## Ans -> 3

