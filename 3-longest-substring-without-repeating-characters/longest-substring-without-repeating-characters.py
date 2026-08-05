class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        left = 0
        result = 0
        if len(s) < 2:
            return len(s)
        for i, right in enumerate(s):

            if right in seen and seen[right] >= left:
                left = seen[right] + 1
            seen[right] = i

            result = max(result , i - left + 1)
        
        return result