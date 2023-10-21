## Insertion Sort  =========================================================================================

## Function Definition

def InsertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = key

    return arr



## Driver Code
arr = [20,40,60,80,40,30,55,100]

## Function Call
result = InsertionSort(arr)
print(result)

## Ans is to be [20, 30, 40, 40, 55, 60, 80, 100]
## time complexity = O(n^2)