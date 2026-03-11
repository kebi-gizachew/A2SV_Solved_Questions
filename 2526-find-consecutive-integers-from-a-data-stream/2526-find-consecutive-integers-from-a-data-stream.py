class DataStream:

    def __init__(self, value: int, k: int):
        self.t = deque()
        self.val = value
        self.k = k
        

    def consec(self, num: int) -> bool:
        if num != self.val:
            self.t.clear()
            return False
        self.t.append(num)
        if len(self.t) < self.k:
            return False
        if len(self.t) > self.k:
            self.t.popleft()
        return True


        

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)