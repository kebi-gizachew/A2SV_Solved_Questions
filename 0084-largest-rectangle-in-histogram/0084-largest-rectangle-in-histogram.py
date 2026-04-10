class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = heights[0]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                stack.pop()
            stack.append(i)
            for k in range(len(stack) - 1, -1 , -1):
                area = max(area , (i - stack[k] + 1) * heights[stack[k]])
            
        return area
















        # left_stack = []
        # right_stack = []
        # i , r = 0 , len(heights) - 1
        # area = 0
        # while r > i:
        #     while left_stack and heights[left_stack[-1]] < heights[i]:
        #         left_stack.pop()
        #     left_stack.append(i)
        #     while right_stack and heights[right_stack[-1]]< heights[r]:
        #         right_stack.pop()
        #     right_stack.append(r)
        #     minn = min(heights[right_stack[0]], heights[left_stack[0]])
        #     right= right_stack[0]
        #     left = left_stack[0]
        #     sub= right - left + 1
        #     area = max(area , minn * sub)
        #     if heights[i] > heights[r]:
        #         r -= 1
        #     else:
        #         i += 1
        # return area
        
        










        # if len(heights) == 1:
        #     return height[0]
        # r , i = len(heights) - 1 , 0
        # area = 0
        # while r > i:
        #     minn= min(heights[i] , heights[r])
        #     diff = r - i +1
        #     area = max(area , diff * minn)
        #     if heights[r] > heights[i]:
        #         i += 1
        #     else:
        #         r -= 1
        # return area





