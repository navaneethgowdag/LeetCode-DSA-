class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def to_days(s):
            m, d = map(int, s.split('-'))
            return sum(months[:m - 1]) + d
        start = max(to_days(arriveAlice), to_days(arriveBob))
        end = min(to_days(leaveAlice), to_days(leaveBob))
        return max(0, end - start + 1)
