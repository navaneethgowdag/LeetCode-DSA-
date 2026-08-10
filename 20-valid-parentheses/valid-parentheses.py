class Solution(object):
    def isValid(self, s):
        if len(s) == 1:
            return False
        bracket = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        i = 0
        while(i != len(s)):
            if s[i] in bracket.values():
                stack.append(s[i])
                i += 1
            elif not stack or bracket[s[i]] != stack[-1]:
                return False
            else:
                stack.pop()
                i += 1
        return len(stack) == 0