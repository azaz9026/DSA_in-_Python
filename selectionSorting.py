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
<<<<<<< HEAD


## Selection Sort (2) -------------------------------------------------------------------------------


## Function Definition
def selectionSort2 (arr2):
    for i in range(len(arr2)):
        min_ele = i
        for j in range(i+1 , len(arr2)):
            if arr2[j] < arr2[min_ele]:
                min_ele = j
        arr2[i] , arr2[min_ele] = arr2[min_ele] , arr2[i]
    return arr2



## Driver code
arr2 = [10,90,40,80,70,70,80,100]

## Function Calling
res = selectionSort2(arr2)
print(res)

=======
>>>>>>> ce5f00515c102587da708535b89b4b7db094b4bd
