class Solution(object):
    def subsets(self, nums):
        res= []
        sol = []

        def recur(i):
            if i == len(nums):
                res.append(sol[:])
                return
            recur(i + 1)
            sol.append(nums[i])
            recur(i + 1)
            sol.pop()
        recur(0)
        return res