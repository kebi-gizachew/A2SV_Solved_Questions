class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        r = set(nums)
        count = 0
        for i in r:
            store = 0
            if i - 1 not in r:
                cur = i 
                while cur in r:
                    cur += 1
                    store += 1
            count = max(count , store)
        return count
                

        




        