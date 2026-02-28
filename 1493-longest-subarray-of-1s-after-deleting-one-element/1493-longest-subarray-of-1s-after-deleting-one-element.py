class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxx = 0
        i = 0
        c = Counter()
        for r in range(len(nums)):
            c[nums[r]] += 1
            if r - i+ 1 - c[1] < 2:
                maxx = max(maxx , r- i + 1)
            if r- i + 1 - c[1] == 2:
                maxx = max(maxx , r- i)
                while nums[i] != 0:
                    c[nums[i]] -= 1
                    i += 1
                c[nums[i]] -= 1
                i += 1
        return maxx - 1
            
