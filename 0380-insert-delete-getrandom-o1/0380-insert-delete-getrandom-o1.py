import random
class RandomizedSet:

    def __init__(self):
        self.temp={}
        self.group=[]
        

    def insert(self, val: int) -> bool:
        if val not in self.temp:
            self.temp[val]=len(self.group)
            self.group.append(val)
            return True
        return False        

    def remove(self, val: int) -> bool:
        if val not in self.temp:
            return False
        x=self.temp[val]
        self.group[x]=self.group[-1]
        t=self.group.pop()
        self.temp[t]=x
        del self.temp[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.group)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()