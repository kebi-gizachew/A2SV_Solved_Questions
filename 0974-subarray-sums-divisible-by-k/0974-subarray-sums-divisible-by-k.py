class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        c = Counter()
        c[0] += 1
        summ = 0
        for r in range(len(nums)):
            summ += nums[r]
            mod = summ% k
            if mod < 0:
                mod += k
            if mod in c:
                count += c[mod]
            c[mod] += 1
        return count

