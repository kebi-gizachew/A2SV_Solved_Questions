class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def divide(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) //2
            left = divide(arr[:mid])
            right = divide(arr[mid:])
            return merge(left,right)

        def merge(left, right):
            res = []
            i , j = 0, 0 
            while i < len(left) and j< len(right):
                if left[i] > right[j]:
                    res.append(right[j])
                    j += 1
                else:
                    res.append(left[i])
                    i += 1
            if i < len(left):
                res.extend(left[i:])
            if j < len(right):
                res.extend(right[j:])
            return res
        return divide(nums)









        # def quick(arr, left , right):
        #     if left >=right:
        #         return
        #     temp= arr[right]
        #     init = left - 1
        #     for i in range(left, right):
        #         if temp >= arr[i]:
        #             init +=1
        #             arr[init] , arr[i] = arr[i] , arr[init]
        #     arr[init + 1] , arr[right] = arr[right] , arr[init + 1]
        #     quick(arr , left , init)
        #     quick(arr , init + 2 , right)
        # quick(nums , 0 , len(nums) - 1)
        # return nums

       






        # # def quick(nums , left , right):
        # #     if right <= left:
        #         return
        #     temp = nums[right]
        #     init = left - 1
        #     for i in range(left , right):
        #         if temp >= nums[i]:
        #             init += 1
        #             nums[init] , nums[i] = nums[i] , nums[init]
        #     nums[init + 1] , nums[right] = nums[right] , nums[init + 1]
        #     quick(nums , left, init)
        #     quick(nums , init + 2 , right)
        # quick(nums , 0 , len(nums) - 1)
        # return nums





        # #     if not nums:
        # #         return []
        # #     temp = nums[-1]
        # #     i = -1
        # #     for k in range(len(nums) - 1):
        # #         if temp >= nums[k]:
        # #             i +=1
        # #             nums[k], nums[i] = nums[i] , nums[k]
        # #     nums[i + 1] , nums[-1] = nums[-1] , nums[i + 1]
        # #     temp1 = quick(nums[:i + 1])
        # #     temp2 = quick(nums[i + 2:])
        # #     return temp1 + nums[i + 1:i + 2] + temp2
           
       
        # # return quick(nums)




        