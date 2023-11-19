## Insertion Sort  =========================================================================================

## Function Definition

def InsertionSort(arrs):
    for i in range(1,len(arrs)):
        key = arrs[i]
        j = i-1
        while key < arrs[j]:
            arrs[j+1] = arrs[j]
            j = j-1

        arrs[j+1] = key

    return arrs



## Driver Code
arrs = [20,40,60,80,40,30,55,100]

## Function Call
result = InsertionSort(arrs)
print(result)

## Ans is to be [20, 30, 40, 40, 55, 60, 80, 100]
## time complexity = O(n^2)
