class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        minn = min(nums)
        maxx = max(nums)
        bucketSize =max(1 , (maxx - minn)// (len(nums) - 1))
        bucketCount = (maxx - minn) // bucketSize + 1
        bucket = [[None , None] for t in range(bucketCount)]
        for i in nums:
            position = (i - minn) // bucketSize
            if bucket[position][0] == None:
                bucket[position][0] = i
                bucket[position][1] = i
            else:
                bucket[position][0] = min(bucket[position][0] , i)
                bucket[position][1] = max(bucket[position][1] , i)
        compare = minn
        max_gap = 0
        for buck in bucket:
            if buck[0]:
                max_gap = max(max_gap , buck[0] - compare)
                compare = buck[1]
        return max_gap




















        # minn = min(nums)
        # temp = [0] * (max(nums) - minn + 1)
        # maxx =0
        # idx = -1 
        # for t in nums:
        #     temp[t - minn] += 1
        # for i in range(len(temp)):
        #     if idx == -1 and temp[i] != 0:
        #         idx = i
        #     elif temp[i] != 0:
        #         maxx = max(maxx , i- idx)
        #         idx = i
        # return maxx



        