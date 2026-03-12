class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 3:
            return 0
        for r in range(len(nums) - 3 , -1, -1):
            if nums[r] + nums[r + 1] > nums[r + 2]:
                return nums[r] + nums[r + 1] + nums[r + 2]
        return 0
        # l , r = len(nums)-3, len(nums) - 1
        # while l>=0:
        #     if nums[l] + nums[l+1] > nums[r]:
        #         return nums[l] + nums[l+1] + nums[r]
        #     l -= 1
        #     r -= 1
        # return 0
