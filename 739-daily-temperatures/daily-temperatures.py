class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                previous = stack.pop()
                answer[previous] = i - previous
            stack.append(i)

        return answer