class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        sell = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i -1]:
                buy = min(buy, prices[i])
            else:
                sell = max(sell, prices[i] - buy)
        if sell > 0:
            return sell
        else:
            return 0