class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(-1, 0), (0 , -1) , (1 , 0), (0, 1)]
        res = []
        pacific = set()
        atlantic = set()
        def ifPass(i , j , visit, val):
            if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]) or heights[i][j] < val or (i , j) in visit:
                return
            visit.add((i , j))
            for x , y in directions:
                ifPass(i + x , j + y , visit, heights[i][j])
        for j in range(len(heights[0])):
            ifPass(0 , j , pacific , -1)
            ifPass(len(heights)- 1 , j , atlantic ,-1)
        for i in range(len(heights)):
            ifPass(i , 0 , pacific , -1)
            ifPass(i , len(heights[0]) - 1 , atlantic , -1)
        for x , y in pacific:
            if (x , y) in atlantic:
                res.append([x , y])
        return res

            











        # pacific = set()
        # atlantic = set()
        # directions = [(-1 , 0) , (1 , 0) , (0 , -1) , (0 , 1)]
        # def ifPass(i , j , val):
        #     if i < 0 or j < 0:
        #         return True
        #     if j >= len(heights[0]) or i >=len(heights[0]):
        #         return False
        #     for x , y in directions:
        #         if ifpass(i + x , j + y):
        #             pacific.add((i , j))
        #         else:
        #             atlantic.add((i , j))
            




















