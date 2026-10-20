class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        l = 0
        best = 0
        length = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            length = r - l + 1
            best = max(length , best)

        return best