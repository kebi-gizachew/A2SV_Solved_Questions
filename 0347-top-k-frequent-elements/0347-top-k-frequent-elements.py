class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rel=Counter(nums)
        arr=[]
        for num,count in rel.items():
            arr.append([count,num])
        arr.sort()
        r=[]
        while len(r)<k:
            r.append(arr.pop()[1])        
        return r
        