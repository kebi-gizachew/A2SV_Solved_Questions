class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for t in range(len(matrix)):
            heappush(heap, (matrix[t][0], t, 0))
        for i in range(k - 1):
            if not heap:
                return -1
            temp, mat_index, index = heappop(heap)
            if index + 1 < len(matrix[mat_index]):
                heappush(heap, (matrix[mat_index][index + 1], mat_index, index + 1))
        return heap[0][0]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna