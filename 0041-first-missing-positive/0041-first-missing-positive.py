class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1] , nums[i] = nums[i] , nums[nums[i] - 1]
        for t in range(len(nums)):
            if nums[t] - 1 != t:
                return t + 1
        return len(nums)+ 1
