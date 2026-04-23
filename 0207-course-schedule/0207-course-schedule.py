class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        gray = set()
        for x , y in prerequisites:
            graph[x].append(y)
        def cycle(node):
            if node in gray:
                return False
            gray.add(node)
            for t in graph[node]:
                if not cycle(t):
                    return False
            gray.remove(node)
            return True
        return cycle(0)















        # graph={i:[] for i in range(numCourses)}
        # for m,n in prerequisites:
        #     graph[n].append(m)
        # visited,visiting=set(),set()
        # def trial(cor):
        #     if cor in visiting:
        #         return False
        #     if cor in visited:
        #         return True
        #     visiting.add(cor)
        #     for t in graph[cor]:
        #         if not trial(t):
        #             return False
        #     visiting.remove(cor)
        #     visited.add(cor)
        #     return True
        # for y in range(numCourses):
        #     if not trial(y):
        #         return False
        # return True 




            






        

        
        