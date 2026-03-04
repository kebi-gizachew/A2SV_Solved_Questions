class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapping = defaultdict(int)
        summ = 0
        count = 0
        for r in range(len(nums)):
            summ +=nums[r]
            if summ== k :
                count += 1
            if summ - k in mapping:
                count += mapping[summ - k]
            mapping[summ]+= 1
        return count



        