class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        c = Counter()
        c[0] += 1
        summ = 0
        for r in range(len(nums)):
            summ += nums[r]
            if summ == goal:
                count += c[0]
            elif summ > goal and summ - goal in c:
                count += c[summ - goal]
            c[summ] += 1
        return count


