class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for t in stones:
            heappush(heap, -t)
        while len(heap) >= 1:
            if len(heap) == 1:
                return -(heap[0])
            largest = -(heappop(heap))
            second = 0
            if heap:
                second = -(heappop(heap))
            if second != largest:
                heappush(heap, second - largest)
        return 0


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna