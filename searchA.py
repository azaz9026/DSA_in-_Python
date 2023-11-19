## Linear Search -----------------------------------------------------------------------------------------------------------

def linearSearch(arr , x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr  = [10 , 20 , 30 , 50 , 40 , 5]
x = 20
res  = linearSearch(arr , x)
print(res)

## binary Search -----------------------------------------------------------------------------------------------------------


def binarySearch(arr1 , l , r , y):
    while l < r :
        mid = l+(r-l)//2
        if arr[mid] == y:
            return mid
        elif arr[mid] > y:
            binarySearch(arr1 , y , mid-1 , l)
        else:
            binarySearch(arr1 , y , mid+1 , r)
    return -1


arr1 = [10 , 20 , 30 , 50 , 40 , 5]
y = 5
l = 0
r = len(arr1)-1
res1  = binarySearch(arr1 , l , r , y)
print(res1)