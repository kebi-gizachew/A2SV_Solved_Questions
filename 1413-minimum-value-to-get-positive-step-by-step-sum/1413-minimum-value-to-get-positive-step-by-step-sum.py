class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        op = 1
        summ = 1
        for r in range(len(nums)):
            summ +=nums[r]
            if summ < 1:
                op += 1- summ
                summ = 1
        return op
        
        