## Selection Sort ----------------------------------------------------------------

## Function Definition

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        # to the min element
        min_idx = i
        for j in range(i+1 , n):
            if arr[j]<arr[min_idx]:
                min_idx = j
                # Swap the element at i and min_idx
        arr[i] , arr[min_idx] = arr[min_idx] , arr[i]
    return arr


## Driver code

arr = [50,38,45,79,19,27,29]

## Function Calling

result = selectionSort(arr)
print(result)

## Ans to be [19, 27, 29, 38, 45, 50, 79]

## Time Complexity :- O(n^2) 
