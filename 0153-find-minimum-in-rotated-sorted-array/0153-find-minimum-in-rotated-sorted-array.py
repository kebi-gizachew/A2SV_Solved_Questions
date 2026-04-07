class Solution:
    def findMin(self, nums: List[int]) -> int:
        left , right = 0 , len(nums) - 1
        ans = 0
        while left <= right:
            mid = left +(right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                if ans == 0:
                    ans= mid
                if nums[mid] < nums[ans]:
                    ans = mid
                right = mid - 1
        return nums[ans]
        