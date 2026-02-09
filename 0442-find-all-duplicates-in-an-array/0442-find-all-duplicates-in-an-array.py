class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        temp=set()
        for i in nums:
            if nums[abs(i)-1]<0:
                temp.add(abs(i))
            nums[abs(i)-1]=-nums[abs(i)-1]
        return list(temp)

