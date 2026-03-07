class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = 0
        cur = nums[0]
        for r in range(len(nums)):
            maxx = max(nums[r] ,maxx + nums[r])
            cur = max(cur , maxx)
        return cur
        # summ = 0
        # finale = float("-inf")
        # minn = 0
        # for r in range(len(nums)):
        #     summ +=nums[r]
        #     finale = max(finale , summ - minn)
        #     minn = min(minn , summ)
        # return finale
        