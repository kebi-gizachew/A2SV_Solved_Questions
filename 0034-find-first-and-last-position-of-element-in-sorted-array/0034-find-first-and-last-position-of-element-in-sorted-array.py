class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def beginner(nums):
            ans = -1
            left , right = 0 , len(nums) - 1
            while right >= left:
                mid= left + (right - left)
                if nums[mid] == target:
                    ans = mid
                    right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1

                else:
                    left = mid + 1
            return ans
        def ending(nums):
            ans = -1
            left , right = 0 , len(nums) - 1
            while right >= left:
                mid= left +(right - left)
                if nums[mid] == target:
                    ans = mid
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return ans
        l = beginner(nums)
        r = ending(nums)
        return [l , r]



            

        