class RecentCounter:

    def __init__(self):
        # self.q=deque()
        self.q = []
        self.start = 0


    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[-1] - self.q[self.start] > 3000:
            self.start += 1
        return len(self.q) - self.start
        # while self.q and t-self.q[0]>3000:
        #     self.q.popleft()
        # self.q.append(t)
        # return len(self.q)
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)