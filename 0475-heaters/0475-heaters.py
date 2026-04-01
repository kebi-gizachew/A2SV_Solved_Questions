class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        left = 0
        right = max(max(houses) , max(heaters))
        ans = right
        def checking(mid):
            temp = houses[0]
            i = 0
            for h in heaters:
                while i < len(houses) and h - mid <= houses[i] <= h + mid:
                    i += 1
    
            if i == len(houses):
                return True
            else:
                return False
          
        while right >= left:
            mid = left + (right - left) // 2
            if checking(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans



        