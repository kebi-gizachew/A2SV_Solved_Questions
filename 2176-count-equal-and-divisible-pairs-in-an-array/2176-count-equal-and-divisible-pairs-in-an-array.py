class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d = defaultdict(list)
        op =0
        if not nums:
            return 0
        for i , j in enumerate(nums):
            d[j].append(i)
        for n , m in d.items():
            if len(m) > 1:
                for j in range(len(m)):
                    for y in range(j+1,len(m)):
                        if m[j] * m[y]% k ==0:
                            op += 1
        return op





        
        