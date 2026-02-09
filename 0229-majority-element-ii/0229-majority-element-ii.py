class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        k=len(nums)//3
        arr=[]
        for i,j in c.items():
            if j>k:
                arr.append(i)
        return arr



        
        