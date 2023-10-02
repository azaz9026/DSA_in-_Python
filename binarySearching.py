## Binary Search -----------------------------------------------------------------------------------------

## In a Sorted Array 

def BinarySearch(arr , i , j , x):
                while i<=j:
                    mid = i + (j - 1)//2
                    if arr[mid] == x:
                        return mid
                    elif arr[mid] < x:
                        BinarySearch(arr , mid+1 , j , x)
                    else:
                        BinarySearch(arr , i , mid-1 , x)
                return-1


arr = [10,20,30,40,50,60,70,80,90,100]
x = 20 
i = 0
j = len(arr)-1
result = BinarySearch(arr , i , j , x )
print(result)