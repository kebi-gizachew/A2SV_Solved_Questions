class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap= []
        for x , y in count.items():
            heappush(heap, (y , x))
            if len(heap) > k:
                heappop(heap)
        return [x for y , x in heap]




        # count = Counter(nums)
        # bucket = [[] for t in range(len(nums) + 1)]
        # for t , freq in count.items():
        #     bucket[freq].append(t)
        # res = []
        # for i in range(len(nums), 0 , -1):
        #     for t in bucket[i]:
        #         res.append(t)
        #         if len(res) == k:
        #             return res









        # rel=Counter(nums)
        # arr=[]
        # for num,count in rel.items():
        #     arr.append([count,num])
        # arr.sort()
        # r=[]
        # while len(r)<k:
        #     r.append(arr.pop()[1])        
        # return r
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna