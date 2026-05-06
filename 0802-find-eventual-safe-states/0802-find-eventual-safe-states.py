class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        d = defaultdict(list)
        for x in range(len(graph)):
            for y in graph[x]:
                d[x].append(y)
        gr = [0 for _ in range(len(graph))]
        def dfs(node):
            if gr[node] == 1:
                return False
            if gr[node] == 2:
                return True
            gr[node] = 1
            for t in d[node]:
                if not dfs(t):
                    return False
            gr[node] = 2
            return True
        for t in range(len(graph)):
            if dfs(t):
                res.append(t)
        return res

        # def dfs(node):
        #     if node in visited:
        #         return False
        #     if not d[node]:
        #         return True
        #     visited.add(node)
        #     for t in d[node]:
        #         if not dfs(t):
        #             return False
        #     res.append(node)
        #     visited.remove(node)
        #     return True
        # for t in range(len(d)):
        #     if t not in visited:
        #         dfs(t)
        # return res

        

        