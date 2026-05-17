class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for i in piles:
            heappush(heap, -i)
        while k > 0:
            temp = -heappop(heap)
            heappush(heap, -((temp + 1) //2))
            k -= 1
        return -(sum(heap))

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna