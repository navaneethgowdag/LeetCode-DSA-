class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) < 1:
            return 0
        result = 1
        seen = set(nums)
        length = 0
        for i in seen:
            if i - 1 not in seen:
                length = 1

                while(i + 1) in seen:
                    length += 1
                    i += 1 

            result = max(length , result)

        return result

