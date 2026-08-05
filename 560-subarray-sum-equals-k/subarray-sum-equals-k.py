class Solution(object):
    def subarraySum(self, nums, k):
        seen = {0:1}
        total = 0
        result = 0
        target = 0
        for i in range(len(nums)):
            total += nums[i]
            target = total - k
            
            if target in seen:
                result += seen[target]
            seen[total] = seen.get(total, 0) + 1
            
        return result