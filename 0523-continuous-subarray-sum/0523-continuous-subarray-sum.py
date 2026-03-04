class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        summ = 0
        mapping = defaultdict(int)
        for r in range(len(nums)):
            summ += nums[r]
            if summ % k == 0 and r > 0:
                return True

            if summ % k in mapping:
                if r - mapping[summ%k] > 1:
                    return True
            else:
                mapping[summ %k] = r
        return False
        