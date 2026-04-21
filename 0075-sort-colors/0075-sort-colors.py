class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quick(left, right):
            if left>= right:
                return 
            temp = nums[right]
            start = left - 1
            for i in range(left, right):
                if temp > nums[i]:
                    start += 1
                    nums[start] , nums[i] = nums[i] , nums[start]
            nums[start + 1] , nums[right] = nums[right] , nums[start+ 1]
            quick(left, start)
            quick(start+ 2 ,right)
        quick(0 , len(nums) -1)
        return nums


        