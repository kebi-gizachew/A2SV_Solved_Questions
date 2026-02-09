class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t=Counter(nums)
        for i in nums:
            if t[i]==1:
                return i
        