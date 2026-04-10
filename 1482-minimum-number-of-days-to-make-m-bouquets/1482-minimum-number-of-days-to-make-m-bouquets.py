class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        left = min(bloomDay)
        right = max(bloomDay)
        ans = -1
        def checking(mid):
            count = 0
            summ = 0
            for i in range(len(bloomDay)):
                flowers = 0
                bouq = 0
                for i in bloomDay:
                    if i <= mid:
                        flowers +=1
                        if flowers == k:
                            bouq += 1
                            flowers = 0
                    else:
                        flowers = 0
                return bouq >= m

            #     if summ >= k:
            #         count += 1
            #         summ = 0
            #     elif bloomDay[i] <= mid:
            #         summ += 1
            #     elif bloomDay[i] > mid:
            #         summ= 0
            # return count >= m

        while right >= left:
            mid = left + (right - left) // 2
            if checking(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
        