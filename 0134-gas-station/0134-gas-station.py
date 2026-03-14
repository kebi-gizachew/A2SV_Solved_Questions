class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        cur = 0
        summ = 0
        for i in range(len(gas)):
            summ += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:
                start = i + 1
                cur = 0
        if summ < 0:
            return -1
        return start


        