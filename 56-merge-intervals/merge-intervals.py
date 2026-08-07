class Solution(object):
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals

        intervals.sort()
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            current = result[-1]
            next_interval = intervals[i]

            if next_interval[0] <= current[1]:
                result[-1] = [
                    current[0],
                    max(current[1], next_interval[1])
                ]
            else:
                result.append(next_interval)

        return result