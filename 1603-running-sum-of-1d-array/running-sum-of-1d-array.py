class Solution(object):
    def runningSum(self, nums):
        add = 0
        for i in range(len(nums)):
            add += nums[i]
            nums[i] = add
        
        return nums