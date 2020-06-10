def maxProfit(prices):
        profit, max_profit = 0, 0
        a = len(prices)
        
        for i in range(1, a):
            profit += prices[i] - prices[i-1]
            max_profit = max(profit, max_profit)
            if profit <= 0:
                profit = 0
        return max_profit



input = [7,1,3,5,6,8]
print(maxProfit(input))




