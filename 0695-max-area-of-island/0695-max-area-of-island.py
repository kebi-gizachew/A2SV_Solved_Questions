class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxx = 0
        directions = [(-1, 0) , (1 , 0), (0, 1), (0 , -1)]
        def countArea(x , y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                grid[x][y] = 0
                temp = 1
                for i , j in directions:
                    temp += countArea(i + x , j + y)
                return temp
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    temp = countArea(i , j)
                    maxx = max(maxx , temp)
        return maxx


        