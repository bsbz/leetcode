'''
        Say you have an array prices for which the ith element is the price of a given stock on day i.

        Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

        Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

        Example 1:

        Input: [7,1,5,3,6,4]
        Output: 7
        Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
                     Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

'''

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




