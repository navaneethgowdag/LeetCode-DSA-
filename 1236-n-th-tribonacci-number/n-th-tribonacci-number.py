class Solution(object):
    def tribonacci(self, n):

        store = {}
        def tri(n):
            if n in store:
                return store[n]
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1
            result = tri(n - 1) + tri(n - 2) + tri(n - 3)
            store[n] = result
            return result
        return tri(n)