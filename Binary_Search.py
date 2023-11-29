# Binary Search Recursion --------------------------


def BinarySearch(arr , i , j , x):
    if arr[i] == x: 
        return i
    else:
        mid = i + (j-i) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return BinarySearch(arr , mid+1 , j , x)
        else:
            return BinarySearch(arr , i , mid , x)
        return -1
    


# Driver Code 

arr = [10,20,30,40,50,60,70,80,90,100]
x = 10
i = 0
j = len(arr)-1

result = BinarySearch(arr , i , j , x )

print(result)