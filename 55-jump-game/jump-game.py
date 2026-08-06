class Solution(object):
    def canJump(self, nums):
        farthest = 0
        for i in range(len(nums)):
            if i <= farthest:
                farthest = max(farthest, nums[i] + i)

            if i > farthest:
                return False

        return True