class Solution(object):
    def rob(self, nums):
        n = len(nums)
        prev2 = 0
        prev1 = 0

        for i in range(n):
            take = prev2 + nums[i]
            skip = prev1

            current = max(take , skip)

            prev2 = prev1
            prev1 = current

        return current
        