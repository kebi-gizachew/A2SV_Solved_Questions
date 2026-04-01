class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = -1
        def check(mid):
            ho = 0
            for i in piles:
                if mid < i:
                    ho += ceil(i / mid)
                else:
                    ho += 1
            if ho > h:
                return False
            return True

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                ans = mid
                right = mid - 1

            else:
                left = mid + 1

        return ans
        