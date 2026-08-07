class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) < 1:
            return 0
        result = 1
        seen = set(nums)
        length = 0
        start = 0
        for i in seen:
            if i - 1 not in seen:
                start = i
                length = 1

                while(start + 1) in seen:
                    length += 1
                    start += 1 

            result = max(length , result)

        return result

