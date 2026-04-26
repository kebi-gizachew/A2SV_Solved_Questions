class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        path = [0]
        visited = set()
        def cycleCycling(val):
            if val == len(graph) - 1:
                res.append(path[:])
                return
            for t in graph[val]:
                path.append(t)
                cycleCycling(t)
                path.pop()
        cycleCycling(0)
        return res
        





















        # path = []
        # res = []
        # visited = set()
        # def circle(val):
        #     if val in visited:
        #         res.append(path[:])
        #         return
        #     path.append(val)
        #     visited.add(val)
        #     if not graph[val]:
        #         res.append(path[:])
        #         return
        #     for t in graph[val]:
        #         circle(t)
        #         path.pop()
        #         visited.remove(t)
        # circle(0)
        # return res




















        #     if val in visited or not graph[val]:
        #         res.append(path[:])
        #     visited.add(val)
        #     for t in graph[val]:
        #         if t not in visited:
        #             path.append(t)
        #             circle(t)
        #         else:
        #             res.append(path[:])
        #         visited.remove(t)
        #     else:
        #         res.append(path[:])
        #     path.pop()
        # circle(0)
        # return res

            



        