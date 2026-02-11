class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        assets = set(nums)
        maxCount = 0
        for i in assets:
            count = 0
            if i - 1 not in assets:
                k = i
                while k in assets:
                    count += 1
                    k = k + 1
            maxCount = max(maxCount , count)
        return maxCount

        # r = set(nums)
        # count = 0
        # for i in r:
        #     store = 0
        #     if i - 1 not in r:
        #         cur = i 
        #         while cur in r:
        #             cur += 1
        #             store += 1
        #     count = max(count , store)
        # return count
                
        

        




        