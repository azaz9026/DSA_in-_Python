## Rotate Array ---------------------------------------------------------------------------------------------


def reverse( arr , low , high ):
    while low < high:
        arr[low] , arr[high] = arr[high] , arr[low]
        low +=1
        high -=1
    return arr

def rotateArray( arr , k ):
    n = len(arr)
    reverse( arr , 0 , n-k-1 )
    reverse( arr , n-k , n-1 )
    reverse( arr , 0 , n-1 )
    return arr


arr = [1,2,3,4,5,6,7]
k = 3
result = rotateArray(arr , k)
print(result)

## Ans => [5, 6, 7, 1, 2, 3, 4]

## The Time complexity => O(n)