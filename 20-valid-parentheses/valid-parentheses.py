class Solution(object):
    def isValid(self, s):
        brace ={
            '}' : '{',
            ')' : '(',
            ']' : '['
        }
        stack = []
        for c in s:
            if c in brace:
                if not stack or stack[-1] != brace[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack
                