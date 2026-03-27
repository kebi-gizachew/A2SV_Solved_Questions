class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottenPoints = deque()
        counter = 0
        directions = [(-1 , 0) , (1 , 0) , (0 , -1) , (0 , 1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rottenPoints.append((i , j))
        while rottenPoints:
            for i in range(len(rottenPoints)):
                x, y= rottenPoints.popleft()
                for n , m in directions:
                    if 0 <= x + n < len(grid) and 0 <= y + m <len(grid[0]) and grid[x +n][y + m] == 1:
                        grid[x +n][y +m] = 2
                        rottenPoints.append((x +n , y + m))
            if rottenPoints:
                counter += 1
        for i in grid:
            if 1 in i:
                return -1
        return counter

        

        


        