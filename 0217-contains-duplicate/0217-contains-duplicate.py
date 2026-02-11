class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        r = list(set(nums))
        return len(r) != len(nums)
        