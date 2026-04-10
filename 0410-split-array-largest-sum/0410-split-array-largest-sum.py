class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        ans = -1
        def checking(mid):
            count = 1
            summ = 0
            for i in range(len(nums)):
                if summ + nums[i] > mid:
                    count += 1
                    summ = nums[i]
                else:
                    summ += nums[i]   
            return count <= k     

        while right >= left:
            mid = left + (right - left) // 2
            if checking(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

















        # minn = float("inf")
        # def trial(arr ,idx):
        #     nonlocal minn
        #     if idx >= len(nums):
        #         m = max(arr)
        #         minn = min(minn , m)
        #         return

        #     for i in range(len(arr)):
        #         arr[i] += nums[idx]
        #         trial(arr , idx +1)
        #         arr[i] -= nums[idx]
        # trial([0] * k , 0)
        # return minn + 1





        