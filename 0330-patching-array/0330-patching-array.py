class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        count = 0
        i = 0
        summ = 0
        while summ < n:
            if i< len(nums) and nums[i] <= summ + 1:
                summ += nums[i]
                i += 1
            else:
                count += 1
                summ += summ + 1
        return count
        