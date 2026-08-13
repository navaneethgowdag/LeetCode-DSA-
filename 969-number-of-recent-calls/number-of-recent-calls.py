from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.req = deque()

    def ping(self, t):
        self.req.append(t)
        while self.req[0] < t - 3000:
            self.req.popleft()
        return len(self.req)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)