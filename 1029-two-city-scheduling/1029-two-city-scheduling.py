class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x:x[0] - x[1])
        summ= 0
        l , r = 0 , len(costs) - 1
        while r > l:
            summ += costs[l][0]
            summ += costs[r][1]
            l += 1
            r -= 1
        return summ

        