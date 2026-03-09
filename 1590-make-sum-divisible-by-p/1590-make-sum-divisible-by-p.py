class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total= sum(nums)
        remain = total % p
        if total < p:
            return -1
        if remain ==0 :
            return 0
        print(remain)
        summ = 0
        c= {0:-1}
        op= len(nums)
        for r in range(len(nums)):
            summ =(summ +nums[r]) % p
            temp = (summ - remain +p) % p
            if temp in c:
                op = min(op , r- c[temp])
            c[summ] = r
        if op == len(nums):
            return -1
        return op
        