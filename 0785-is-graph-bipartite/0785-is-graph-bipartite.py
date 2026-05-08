class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0 for _ in range(len(graph))]
        d = defaultdict(list)
        visited = set()
        for i in range(len(graph)):
            for j in graph[i]:
                d[i].append(j)
        def dfs(node, cur):
            if color[node] == 1 and cur == 2:
                return False
            if color[node] == 2 and cur == 1:
                return False
            if node in visited or color[node] == cur:
                return True
            color[node] = cur
            cur = 2 if cur == 1 else 1
            for t in d[node]:
                if not dfs(t , cur):
                    return False
            visited.add(node)
            return True
        for i in range(len(graph)):
            if color[i] == 0 and not dfs(i, 1):
                return False
        return True
















        # white , black = 1 , 0
        # d = {i : -1 for i in range(len(graph))}
        # def cycleCycling(val , Color):
        #     if d[val] == Color:
        #         return True
        #     elif d[val] == 1 - Color:
        #         return False
        #     d[val] = Color
        #     for t in graph[val]:
        #         if not cycleCycling(t , 1 - Color):
        #             return False
        #     return True
        # for y in range(len(graph)):
        #     if d[y] == -1:
        #         if not cycleCycling(y , white):
        #             return False
        # return True











      












        # black = set()
        # white = set()
        # def traverse(i , flag):
        #     if i in black:
        #         return flag == 0
        #     if i in white:
        #         return flag == 1
            
        #     if flag == 1:
        #         white.add(i)
        #         flag = 0
        #     else:
        #         black.add(i)
        #         flag = 1
           
        #     for row in graph[i]:
        #         if not traverse(row , flag):
        #             return False
        #     return True
        # for i in range(len(graph)):
        #     if i not in black and i not in white:
        #         if not traverse(i , 1):
        #             return False
        # return True

        