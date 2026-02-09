class FrequencyTracker:

    def __init__(self):
        self.freq = {}
        self.rev = {}
        

    def add(self, number: int) -> None:
        x=0
        if number in self.freq:
            x=self.freq[number]
        self.freq[number] = self.freq.get(number , 0) + 1
        if x!=0:
            self.rev[x]-=1
            if self.rev[x]==0:
                del self.rev[x]
        self.rev[self.freq[number]] = self.rev.get(self.freq[number], 0) + 1
        

    def deleteOne(self, number: int) -> None:
        if number in self.freq:
            x = self.freq[number]
            self.freq[number]-=1
            if self.freq[number] == 0:
                del self.freq[number]
            self.rev[x] -= 1
            if self.rev[x] == 0:
                del self.rev[x]
            if number in self.freq:
                self.rev[self.freq[number]] = self.rev.get(self.freq[number], 0) + 1

        
        
    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.rev:
            return True
        return False


        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)