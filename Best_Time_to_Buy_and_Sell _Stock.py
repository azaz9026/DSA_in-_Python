
##Best Time to Buy and Sell Stock

def max_profit(prices, n):
    buy = prices[0]
    maxi = 0
    
    for i in range(n):
        if buy < prices[i]:
            buy = prices[i]
        elif maxi < buy - prices[i]:
            maxi = buy - prices[i]
    return maxi

prices = [7, 1, 5, 3, 6, 4]
n = len(prices)

res = max_profit(prices, n)
print(res)
