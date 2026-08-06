class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        sell = 0
        best_sell = 0
        best_buy = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                best_sell = prices[i] - buy
                sell = max(sell, best_sell)
            else:
                best_buy = prices[i]
                buy = min(buy, best_buy)
        if sell > 0:
            return sell
        else:
            return 0