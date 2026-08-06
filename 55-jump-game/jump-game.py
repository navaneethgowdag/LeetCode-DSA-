class Solution(object):
    def canJump(self, nums):
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False

            farthest = max(farthest, nums[i] + i)

        return True