## (Qus :- 1)  Best time to Buy & Sell Stock

## function Definition

def findMaxProfit(price):
    min_price = float('inf')
    max_profit = 0

    for i in range(len(price)):
        if price[i] < min_price:
            min_price = price[i]
        elif price[i] - min_price > max_profit:
            max_profit = price[i] - min_price
    return max_profit


price = [7,1,5,8,9,3,4,10]
maxProfit = findMaxProfit(price)

print(maxProfit)

## the Ans Should be 14 ---------------------->  the max_ profit is to be this one  9
## Time Complexity O(n)
## Space Complexity O(1)


## /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


## (Qus :- 2)  Collinear point


## function Definition

def collinearPoint(x1 , x2 , x3 , y1 , y2 , y3):
    if ((y2-y1)*(x3-x2) == (y3-y2)*(x2-x1)):
        print('The given point are Collinear')
    else:
       print('The given point are Non-Collinear')


x1 , x2 , x3 , y1 , y2 , y3 = 1 , 1 , 1 , 6 , 0 , 9

## Function Calling 
res1 = collinearPoint(x1 , x2 , x3 , y1 , y2 , y3)
print(res1)
## the Ans Should be  ---------------------->  The given point are Collinear.
## Time Complexity O(1)
## Space Complexity O(1)



## /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


## (Qus :- 3)  Collinear point other method 


## function Definition

def collinearPoint2(x1,x2,x3,y1,y2,y3):

    area = 0.5 * (x1 * (y2-y3) + x2 * (y3-y1) + x3 * (y1-y2))
    if area == 0:
        print('The given point are Collinear')
    else:
        print('The given point are Non-Collinear')
       

x1 = 1 
x2 = 1 
x3 = 1
y1 = 6 
y2 = 0 
y3 = 9

## Function Calling 

collinearPoint2(x1,x2,x3,y1,y2,y3)

## the Ans Should be  ---------------------->  The given point are Collinear.
## Time Complexity O(1)
## Space Complexity O(1)


## /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


## (Qus :- 4)  Majority Element 

## Function Deffinition
from collections import Counter

def majorityElement(nums):
    counts = Counter(nums)
    print(counts)
    return max(counts.keys() , key = counts.get)



nums  =  [1,1,1,1,2,2,2,1,1,2,2]
result = majorityElement(nums)
print(result)




## (Qus :- 5)  Collinear point other method 


## Function Deffinition

def colorSort(num):
    p0 = curr = 0
    p2 = len(num)-1
    while curr <= p2:
        if num[curr] == 0:
            num[p0] , num[curr] = num[curr] , num[p0]
            p0 += 1
            curr += 1
        elif num[curr] == 2:
            num[p2] , num[curr] = num[curr] , num[p2]
            p2 -= 1
        else:
            curr += 1
    return num


num = [2,0,2,0,1,1]
result = colorSort(num)
print(result)


### //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
## by Bubble Sort

def colorSort2(num2):
    n = len(num2)
    for i in range(n):
        for j in range(n-i-1):
            if num2[j] > num2[j+1]:
                num2[j] , num2[j+1] =  num2[j+1] , num2[j]
    return num2




num2 = [2,0,2,0,1,1]
result = colorSort2(num2)
print(result)



## the Ans Should be  ---------------------->  [0, 0, 1, 1, 2, 2] all color are sorted.
## Time Complexity O(n)
## Space Complexity O(1)


