class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            while nums[i] != nums[nums[i]-1]:
                temp = nums[i] - 1
                nums[i] , nums[temp] = nums[temp] , nums[i]
        print(nums)
        for k in range(len(nums)):
            if nums[k] != k+ 1:
                res.append(nums[k])
        return res








        # temp=Counter()
        # arr=[]
        # for i in nums:
        #     if i in temp:
        #         arr.append(i)
        #     else:
        #         temp[i]+=1
        # return arr


        # # temp=set()
        # # for i in nums:
        # #     if nums[abs(i)-1]<0:
        # #         temp.add(abs(i))
        # #     nums[abs(i)-1]=-nums[abs(i)-1]
        # # return list(temp)

