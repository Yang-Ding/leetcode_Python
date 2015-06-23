from sys import maxint
class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        low=maxint
        maxprofit=0
        for i in range(len(prices)):
            if prices[i]-low>maxprofit:
                maxprofit=prices[i]-low
            if prices[i]<low:
                low=prices[i]
        return maxprofit
