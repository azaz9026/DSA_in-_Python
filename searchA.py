## Linear Search -----------------------------------------------------------------------------------------------------------

def linearSearch(arr , x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr  = [10 , 20 , 30 , 50 , 40 , 5]
x = 200
res  = linearSearch(arr , x)
print(res)



## binary Search -----------------------------------------------------------------------------------------------------------


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
x = 1000
i = 0
j = len(arr)-1

result = BinarySearch(arr , i , j , x )

print(result)



## Ternay Search -----------------------------------------------------------------------------------------------------------

def ternaySearch(arr , i , j , x):
    while i<=j:
        mid_1 = i+(j-i)//3
        mid_2 = i-(i-j)//3

        if arr[mid_1] == x:
            return mid_1
        elif arr[mid_2] == x:
            return mid_2
        elif arr[mid_1] > x:
            j = mid_1 - 1
        elif arr[mid_2] < x:
            i = mid_2 + 1
        else:
            mid_1+1 , mid_2-1
    return -1

arr = [10,20,30,40,50,60,70,80,90,100]
x = 1000
i = 0
j = len(arr)-1

result = ternaySearch(arr , i , j , x )

print(result)