class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        profit=0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                profit+=(prices[i+1]-prices[i])
        return profit
