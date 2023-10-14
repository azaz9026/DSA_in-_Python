## 1 Binary Search -----------------------------------------------------------------------------------------


## In a Sorted Array 



def teranrySearch(arr , i , j , x):
    while i<=j:
        midpoint1=i+(j-i)//3
        midpoint2=j-(i-j)//3
        if arr[midpoint1]==x:
            return midpoint1
        elif arr[midpoint2]==x:
            return midpoint2
        elif x < arr[midpoint1]:
            j = midpoint1 - 1
        elif x > arr[midpoint2]:
            i = midpoint2 + 1
        else:
            midpoint1 + 1 , midpoint2 + 1
    return - 1
             

arr = [10,20,30,40,50,60,70,80,90,100]
x = 100
i = 0
j = len(arr)-1

result = teranrySearch(arr , i , j , x )

print(result)



