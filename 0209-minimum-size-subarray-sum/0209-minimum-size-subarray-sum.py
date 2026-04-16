class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minn = float("inf")
        c = {0: -1}
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            if summ - target in c:
                minn = min(minn , i - c[summ - target])
            c[summ] = i
        return minn if minn != float("inf") else 0





        













        # summ = 0
        # c = {0: -1}
        # minn = float("inf")
        # for r in range(len(nums)):
        #     summ += nums[r]
        #     if summ - target in c:
        #         minn= min(minn , r - c[summ - target])
        #     c[summ]= r
        # return minn if minn!=float("inf") else 0


        