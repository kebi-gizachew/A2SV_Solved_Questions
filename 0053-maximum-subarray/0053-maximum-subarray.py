class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        minn = 0
        summ = 0
        maxx = nums[0]
        for i in range(len(nums)):
            summ += nums[i]
            maxx = max(maxx , summ - minn)
            minn = min(minn , summ)
        return maxx
        # maxx = nums[0]
        # cur = nums[0]
        # for i in range(len(nums)):
        #     cur = max(cur + nums[i] , nums[i])
        #     maxx = max(maxx , cur)















        # maxx = nums[0]
        # cur = 0
        # for i in range(len(nums)):
        #     cur = max(nums[i] , cur + nums[i])
        #     maxx = max(maxx , cur)
        # return maxx

        # minn = 0
        # summ = 0
        # maxx = 0
        # for i in range(len(nums)):
        #     summ += nums[i]
        #     maxx = max(maxx , summ - minn)
        #     minn = min(minn , summ)
        # return maxx







        # # maxx = 0
        # # cur = nums[0]
        # # for r in range(len(nums)):
        # #     maxx = max(nums[r] ,maxx + nums[r])
        # #     cur = max(cur , maxx)
        # # return cur





        # summ = 0
        # finale = float("-inf")
        # minn = 0
        # for r in range(len(nums)):
        #     summ +=nums[r]
        #     finale = max(finale , summ - minn)
        #     minn = min(minn , summ)
        # return finale
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna