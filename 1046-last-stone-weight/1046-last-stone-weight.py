class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapify(heap)
        while len(heap) > 1:
            v1 = -heappop(heap)
            v2 = -heappop(heap)
            if v1 != v2:
                heappush(heap, -abs(v1 - v2))
        if heap:
            return -heap[0]
        return 0

        
















        # heap = []
        # for t in stones:
        #     heappush(heap, -t)
        # while len(heap) >= 1:
        #     if len(heap) == 1:
        #         return -(heap[0])
        #     largest = -(heappop(heap))
        #     second = 0
        #     if heap:
        #         second = -(heappop(heap))
        #     if second != largest:
        #         heappush(heap, second - largest)
        # return 0


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna