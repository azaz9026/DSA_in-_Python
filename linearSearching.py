##  Linear Search -------------------------------------------------------------------------------------

## arr = [10,20,30,40,50,60,70,80,90,100]
## X =  any  element
## n = len(arr)

    ## for i in range(n):
    ##    if arr[i] == x:
    ##        return i
    ## return -1



def Linearsearch(arr , x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


## Driver Code

arr = [10,20,30,40,50,60,70,80,90,100]
x = 5

## funtion Calling 

result = Linearsearch( arr , x )
print(result)

## Time Complexity O(n)
## Space Complexity O(1)


