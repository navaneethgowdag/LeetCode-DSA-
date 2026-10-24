class Solution(object):
    def climbStairs(self, n):
        store = {}
        def climb(n):
            if n in store:
                return store[n]
            if n == 1:
                return 1
            if n== 2:
                return 2
            result = climb(n - 1) + climb(n-2)
            store[n] = result
            return result
        return climb(n)  