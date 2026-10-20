class Solution(object):
    def longestOnes(self, nums, k):
        l = 0
        best = 0
        zeros = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1            
                while zeros > k:
                    if nums[l] == 0:
                        zeros -= 1
                    l += 1
            best = max(best, r - l + 1)

        return best 