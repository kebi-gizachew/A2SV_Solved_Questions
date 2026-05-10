class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        d = {0 :-1}
        target = sum(nums) % p
        summ = 0
        if target == 0:
            return 0
        if sum(nums) < p:
            return -1
        minn = len(nums)
        for i in range(len(nums)):
            summ += nums[i]
            temp = summ % p
            val = (p - target + temp) %p
            if val in d:
                minn = min(i - d[val], minn)
            d[temp] = i
        return minn if minn != len(nums) else -1
        # total= sum(nums)
        # remain = total % p
        # if total < p:
        #     return -1
        # if remain ==0 :
        #     return 0
        # print(remain)
        # summ = 0
        # c= {0:-1}
        # op= len(nums)
        # for r in range(len(nums)):
        #     summ =(summ +nums[r]) % p
        #     temp = (summ - remain +p) % p
        #     if temp in c:
        #         op = min(op , r- c[temp])
        #     c[summ] = r
        # if op == len(nums):
        #     return -1
        # return op
        