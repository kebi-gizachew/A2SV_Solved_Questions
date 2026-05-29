class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        directions = [(0 , 1) , (1 , 0), (0 , -1), (-1 , 0)]
        def dfs(i , j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            count = 0
            grid[i][j] = 0
            for x , y in directions:
                count += dfs(x + i , y + j)
            return count + 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area , dfs(i ,j))
        return max_area
            














        # directions = [(-1 , 0) , (1 , 0) , (0 , -1), (0 , 1)]
        # maxx = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #             grid[i][j] = 0
        #             count = 1
        #             queue = deque()
        #             queue.append((i , j))
        #             while queue:
        #                 x , y = queue.popleft()
        #                 for dirX , dirY in directions:
        #                     if 0 <= x + dirX < len(grid) and 0 <= y + dirY < len(grid[0]) and grid[x +dirX][y + dirY] == 1:
        #                         grid[x + dirX][y +dirY] = 0
        #                         queue.append((x + dirX, y +dirY))
        #                         count += 1
        #             maxx = max(maxx , count)
        # return maxx














        # maxx = 0
        # directions = [(-1, 0) , (1 , 0), (0, 1), (0 , -1)]
        # def countArea(x , y):
        #     if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
        #         grid[x][y] = 0
        #         temp = 1
        #         for i , j in directions:
        #             temp += countArea(i + x , j + y)
        #         return temp
        #     return 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #             temp = countArea(i , j)
        #             maxx = max(maxx , temp)
        # return maxx


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna