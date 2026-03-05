class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        r = [0]* (len(nums) + 1)
        nums.sort()
        for x , y in requests:
            r[x] += 1
            r[y +1] -= 1
        for t in range(1 , len(nums)):
            r[t] = r[t] + r[t-1]
        r.pop()
        r.sort()
        op = 0
        while r and nums and r[-1] != 0 :
            op += r.pop() * nums.pop()
        return op % (10**9 + 7)



        
        