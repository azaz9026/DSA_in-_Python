## Find the Duplicate Number ---------------------------------------------------------------------------

def duplicateNumber(arr):
    arr = sorted(arr)  # or arr.sort()
    duplicates = 0
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            duplicates = arr[i]
            return duplicates

arr = [1, 3, 2, 4, 2]
result = duplicateNumber(arr)
print(result)


## By HashSet or Hashmap