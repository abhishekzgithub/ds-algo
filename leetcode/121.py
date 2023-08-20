"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

----
just keep a look at the sell side, if sell is smaller,swap it will buy and move ahead.
"""

class Solution:
    def maxProfit(self, prices):
        sell=1
        buy=0
        max_profit=0
        while sell<len(prices):
            profit=prices[sell]-prices[buy]
            if prices[sell]>prices[buy]:
                max_profit=max(max_profit, profit)
            else:
                buy=sell
            sell+=1
        return max_profit

    def maxProfit(self,prices):
        """
        selling index will keep on increasing
        we have to find buy and sell index
        not to confuse with already bought
        """
        buy,sell=0,1
        max_profit=0
        while sell<len(prices):
            profit=prices[sell]-prices[buy]
            if prices[buy]>prices[sell]:
                buy=sell
            max_profit=max(profit,max_profit)
            sell+=1
        return max_profit


prices = [7,1,5,3,6,4] #output =5

print(Solution().maxProfit(prices))