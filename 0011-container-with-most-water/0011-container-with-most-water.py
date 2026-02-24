class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        r = len(height) - 1
        op = 0
        while i < r:
            area = min(height[i] , height[r]) * (r - i)
            op = max(op , area)
            if height[i] > height[r]:
                r -= 1
            else:
                i += 1
        return op

        