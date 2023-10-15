## Bubble Sort ----------------------------------------------------------------------------------------



## Method Definition

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                ## Swap the element
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr



## Driver Code

arr = [70,20,30,40,5,0,10,60,100]
result = bubbleSort(arr)
print(result)


## Ans :- [0, 5, 10, 20, 30, 40, 60, 70, 100]
## it was the Sort Array