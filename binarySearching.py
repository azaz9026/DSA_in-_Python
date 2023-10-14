## 1 Binary Search -----------------------------------------------------------------------------------------

## In a Sorted Array 


def BinarySearch(arr , i , j , x):
    while i <= j:
        midpoint = i+(j-i)//2
        if arr[midpoint]==x:
            return midpoint
        elif arr[midpoint]<x:
            return BinarySearch(arr , midpoint+1 , j , x)
        else:
            return BinarySearch(arr , i , midpoint-1 , x)
    return -1
               


arr = [10,20,30,40,50,60,70,80,90,100]
x = 100
i = 0
j = len(arr)-1
result = BinarySearch(arr , i , j , x )
print(result)


## 2 Binary Search -----------------------------------------------------------------------------------------


def Binary(arr1 , i , j , x):
    while i <= j:
        mids = i+(j - i)//2
        if arr1[mids]==x:
            return mids
        elif arr1[mids]<x:
            i = mids + 1
        else:
            j = mids - 1
    return -1


arr1 = [1,2,3,4,5,6,7,8,9]
x = 5
i = 0
j = len(arr1)-1
results = Binary(arr1 , i , j , x )
print(results)

