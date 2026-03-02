class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        temp = 0
        i = 0
        c = Counter()
        for r in range(len(nums)):
            c[nums[r]] += 1
            while len(c) > k:
                c[nums[i]] -= 1
                if c[nums[i]] == 0:
                    del c[nums[i]]
                i += 1
            temp += r-i + 1
        d = Counter()
        j = 0
        temp1 = 0
        for r in range(len(nums)):
            d[nums[r]] += 1
            while len(d) > k - 1:
                d[nums[j]] -= 1
                if d[nums[j]] == 0:
                    del d[nums[j]]
                j += 1
            temp -= r-j + 1
        return temp 


        