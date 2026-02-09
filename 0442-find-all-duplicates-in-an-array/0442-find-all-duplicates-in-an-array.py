class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        temp=Counter()
        arr=[]
        for i in nums:
            if i in temp:
                arr.append(i)
            else:
                temp[i]+=1
        return arr

