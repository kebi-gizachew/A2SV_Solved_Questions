class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        ans = -1
        def checking(mid):
            day = 1
            summ = 0
            for i in range(len(weights)):
                if summ + weights[i] > mid:
                    day += 1
                    summ = 0
                if day > days:
                    return False
                summ += weights[i]
            return True


        def trial(left , right):
            nonlocal ans
            if left > right:
                return
            mid = left + (right - left)//2
            if checking(mid):
                ans= mid
                trial(left , mid - 1)
            else:
                trial(mid + 1 ,right)
        trial(left , right)
        return ans

        