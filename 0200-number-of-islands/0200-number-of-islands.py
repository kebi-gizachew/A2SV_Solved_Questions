class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # visited = set()
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == "1":
        #             visited.append((i, j))
        def iterateGrid(i , j):
            if i <0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
                return
            # visited.remove((i , j))
            grid[i][j] = "0"
            iterateGrid(i + 1 , j)
            iterateGrid(i - 1 , j)
            iterateGrid(i , j + 1)
            iterateGrid(i , j - 1)
        # v = list(visited)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    iterateGrid(i , j)
        return count









        # if not grid:
        #     return 0
        # row,col=len(grid),len(grid[0])
        # def dfs(r,c):
        #     if(r<0 or r>=row or c<0 or c>=col or grid[r][c]=="0"):
        #         return
        #     grid[r][c]="0"
        #     dfs(r+1,c)
        #     dfs(r-1,c)
        #     dfs(r,c+1)
        #     dfs(r,c-1)
        # count=0
        # for i in range(row):
        #     for t in range(col):
        #         if(grid[i][t]=="1"):
        #             count+=1
        #             dfs(i,t)
                
        # return count
       

        