class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i] , nums[nums[i] -1]
        for k in range(len(nums)):
            if k + 1 != nums[k]:
                return [nums[k] , k +1]
            
            
        
                

        