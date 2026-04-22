class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        black = set()
        white = set()
        def traverse(i , flag):
            if i in black:
                return flag == 0
            if i in white:
                return flag == 1
            
            if flag == 1:
                white.add(i)
                flag = 0
            else:
                black.add(i)
                flag = 1
           
            for row in graph[i]:
                if not traverse(row , flag):
                    return False
            return True
        for i in range(len(graph)):
            if i not in black and i not in white:
                if not traverse(0 , 1):
                    return False
        return True

        