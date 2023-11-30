
##Best Time to Buy and Sell Stock

def max_profit(prices, n):
    minimum = prices[0]
    profit = 0
    for i in range(1, n):
        profit = max(profit, prices[i] - minimum)
        minimum = min(minimum, prices[i])
    return profit

prices = [7, 1, 5, 3, 6, 4]
n = len(prices)

res = max_profit(prices, n)
print(res)







def max_profit(prices, n):
    maximum = 0
    for i in range(0, n-1):
        for j in range(i+1, n):  # Start from i+1
            maximum = max(maximum, prices[j] - prices[i])
        
    return maximum

prices = [7, 1, 5, 3, 6, 4]
n = len(prices)

result = max_profit(prices, n)
print(result) 
