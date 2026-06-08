class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        def dfs(indx, lad, brick, count):
            if indx + 1 >= len(heights):
                return count
            diff = heights[indx +1] - heights[indx]
            r = 0
            maxx = 0
            if diff < 0:
                r = dfs(indx + 1, lad , brick, count + 1)
                return r
            if brick - diff >= 0:
                maxx = max(maxx , dfs(indx + 1, lad, brick - diff, count + 1))
            if lad > 0:
                maxx = max(maxx , dfs(indx + 1, lad -1, brick, count + 1))
            if brick - diff <= 0 and lad == 0:
                return count

            return maxx
        return dfs(0 , ladders, bricks, 0)
                













        # heap = []
        # for i in range(1 , len(heights)):
        #     diff_heights = heights[i] - heights[i - 1]
        #     if diff_heights > 0:
        #         heapq.heappush(heap , diff_heights)
        #         if len(heap) > ladders:
        #             bricks -= heapq.heappop(heap)
        #         if bricks < 0:
        #             return i -1
        # return len(heights) - 1

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna