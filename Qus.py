## (Qus :- 1)  Best time to Buy & Sell Stock

## function Definition

def findMaxProfit(prices):
    min_Prices = float('inf')
    max_profit = 0

    for i in range (len(prices)):
        if prices[i] < min_Prices:
            min_Prices = prices[i]
        elif prices[i] - min_Prices > max_profit:
            max_profit = prices[i] - min_Prices
    return max_profit


prices = [7,1,5,3,6,4,15]

## Function Calling 

result = findMaxProfit(prices)
print(" the max_ profit is to be this one " , result)

## the Ans Should be 14 ---------------------->  the max_ profit is to be this one  14



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
collinearPoint(x1 , x2 , x3 , y1 , y2 , y3)

## the Ans Should be  ---------------------->  The given point are Collinear.




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