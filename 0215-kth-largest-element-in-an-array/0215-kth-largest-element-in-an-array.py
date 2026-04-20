class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick(left, right):
            nonlocal k
            if left> right:
                return -1
            temp = nums[right]
            init= left - 1
            for i in range(left, right):
                if temp >=nums[i]:
                    init += 1
                    nums[init] , nums[i] = nums[i] , nums[init]
            if init + 1 == len(nums) - k:
                return temp
            nums[init + 1] , nums[right] = nums[right] , nums[init + 1]
            if quick(left, init) == -1:
                return quick(init + 2 , right)
            else:
                return quick(left , init)
        return quick(0 , len(nums) - 1)        












        # def divide(nums):
        #     if len(nums) <= 1:
        #         return nums
        #     arr = []
        #     mid = len(nums) // 2
        #     left = divide(nums[:mid])
        #     right = divide(nums[mid:])
        #     i , j = 0 , 0
        #     while i < len(left) and j < len(right):
        #         if left[i] > right[j]:
        #             arr.append(right[j])
        #             j +=1 
        #         else:
        #             arr.append(left[i])
        #             i += 1
        #     return arr
        # t = divide(nums)
        # return t[len(nums) - k]









        def quick(nums , left , right):
            nonlocal k
            num = nums[right]
            i = left - 1
            for j in range(left , right):
                if nums[j] <= num:
                    nums[i + 1] ,nums[j] = nums[j] , nums[i + 1]
                    i += 1
            nums[i + 1] , nums[right] = nums[right] , nums[i + 1]
            if i + 1 == len(nums) - k:
                return num
            elif (i + 1) < (len(nums) - k):
                return quick(nums , i + 2 , right)
            else:
                return quick(nums , left , i)

        return quick(nums , 0 , len(nums) - 1)

            




        # k = nums[0]
        # for i in range(len(nums)):
        #     k = max(k , nums[i])

        