class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        nums = {}
        a = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                a = grid[i][j]
                nums[grid[i][j]] = nums.get(grid[i][j], 0) + 1

        repeated = missing = None
        for i in range(1, len(grid) * len(grid) + 1):
            if i in nums and nums[i] == 2:
                repeated = i
            if i not in nums:
                missing = i
        
        return [repeated, missing]