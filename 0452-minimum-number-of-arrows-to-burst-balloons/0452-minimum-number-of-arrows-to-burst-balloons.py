class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        op = 1
        points.sort(key = lambda x :x[0])
        temp = points[0]
        for i , j in points[1:]:
            if temp[1] >= i:
                x = min(temp[1] , j)
                y = max(temp[0], i)
                temp = [y , x]
            else:
                op += 1
                temp= [i , j]
        return op
