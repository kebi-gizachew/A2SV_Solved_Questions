class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        inbound = set()
        directions = [(-1, 0) , (0 , -1) , (1 , 0) , (0 , 1)]
        def land(i , j):
            nonlocal count
            if i < 0 or j <0 or j >= len(grid[0]) or i >= len(grid) or grid[i][j] == 0:
                count += 1
                return
            if (i, j) in inbound:
                return
            inbound.add((i , j))
            for x , y in directions:
                land(i + x , j + y)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    land(i , j)
        return count

        