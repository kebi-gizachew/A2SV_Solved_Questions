class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sums=0
        arr=[]
        for i in nums:
            if i%2==0:
                sums+=i
        for n,m in queries:
            if nums[m]%2==0:
                sums-=nums[m]
            nums[m]+=n
            if nums[m]%2==0:
                sums+=nums[m]
            arr.append(sums)
        return arr
            
                
            
        