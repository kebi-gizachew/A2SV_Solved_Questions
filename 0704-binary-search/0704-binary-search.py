class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left +(right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid- 1
            else:
                left = mid + 1
        return -1

       
        # def trial(num , left,right):
        #     if left > right:
        #         return -1
        #     mid = left + (right - left) //2
        #     if mid== target:
        #         return mid
        #     if mid > target:
        #         return trial(num ,left, mid - 1)
        #     else:
        #         return trial(num ,mid + 1 , right)
        # return trial(nums , 0 , len(nums) -1)

        