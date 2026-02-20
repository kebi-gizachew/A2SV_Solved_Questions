class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        tempo=[]
        result=[0]*len(nums)
        for i in range(len(nums)):
            tempo.append((nums[i],i))
        tem=sorted(tempo,key=lambda x:x[0])
        for t,k in enumerate(tem):
            m,n=k
            if t>0 and tem[t-1][0]==tem[t][0]:
                result[n]=result[tem[t-1][1]]
            else:
                result[n]=t
        return result



        
        






        