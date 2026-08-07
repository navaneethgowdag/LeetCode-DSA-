class Solution(object):
    def productExceptSelf(self, nums):

        prefix = 1
        suffix = 1
        result = [1] * len(nums)
        
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) -1 , -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result