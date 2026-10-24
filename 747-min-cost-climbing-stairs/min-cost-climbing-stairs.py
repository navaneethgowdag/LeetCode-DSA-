class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        answer = [0] * n
        answer[0] = cost[0]
        answer[1] = cost[1]
        for i in range(2, n):
            answer[i] = min(answer[i - 2], answer[i -1]) + cost[i]
        return min(answer[n-1], answer[n-2])