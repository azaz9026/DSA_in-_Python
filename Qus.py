## Best time to Buy & Sell Stock

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
