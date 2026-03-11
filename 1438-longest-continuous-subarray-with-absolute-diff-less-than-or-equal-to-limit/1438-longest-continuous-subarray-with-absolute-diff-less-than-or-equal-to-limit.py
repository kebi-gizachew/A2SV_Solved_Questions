class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        maxx = deque()
        minn = deque()
        k = 0
        res = 0
        for r in range(len(nums)):
            while maxx and maxx[-1] < nums[r]:
                maxx.pop()
            maxx.append(nums[r])
            while minn and minn[-1] > nums[r]:
                minn.pop()
            minn.append(nums[r])
            while maxx[0] - minn[0] > limit:
                if nums[k] == maxx[0]:
                    maxx.popleft()
                if nums[k] == minn[0]:
                    minn.popleft()
                k += 1
            res= max(res , r - k + 1)
        return res
        










        # maxs=deque()
        # mins=deque()
        # k=0
        # difference=0
        # for i in range(len(nums)):
        #     if not maxs:
        #         maxs.append(nums[i])
        #     if not mins:
        #         mins.append(nums[i])
        #     else:
        #         while maxs and maxs[-1]<nums[i]:
        #             maxs.pop()
        #         maxs.append(nums[i])
        #         while mins and mins[-1]>nums[i]:
        #             mins.pop()
        #         mins.append(nums[i])
        #         while maxs[0]-mins[0]>limit:
        #             if maxs[0]==nums[k]:
        #                 maxs.popleft()
        #             if mins[0]==nums[k]:
        #                 mins.popleft()
        #             k+=1
        #     difference=max(difference,i-k+1)
        # return difference
            
            
            
        