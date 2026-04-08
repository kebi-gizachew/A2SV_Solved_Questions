class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        ans = 0
        left = 1
        right = max(candies)
        def check(mid):
            count = 0
            for i in range(len(candies)):
                if candies[i] >= mid:
                    count += candies[i] // mid
            return count >= k
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

        