class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sets=defaultdict(int)
        for i ,val in enumerate(nums):
            t=target-val
            if t in sets:
                return [sets[t],i]
            sets[val]=i
            
