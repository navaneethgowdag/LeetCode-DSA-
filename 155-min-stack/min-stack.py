class MinStack(object):

    def __init__(self):
        global stack, min_stack
        stack = []
        min_stack = []

    def push(self, value):
        if len(min_stack) == 0:
            min_stack.append(value)
        else:
            min_stack.append(min(value, min_stack[-1]))

        return stack.append(value)
        

    def pop(self):
        stack.pop()
        min_stack.pop()

    def top(self):
        return stack[-1]
        

    def getMin(self):
        return min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()