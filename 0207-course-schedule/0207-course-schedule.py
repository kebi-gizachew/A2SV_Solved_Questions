class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        color = [0 for i in range(numCourses)]
        d= defaultdict(list)
        for x, y in prerequisites:
            d[y].append(x)
        def dfs(node):
            if color[node] == 1:
                return False
            if color[node] == 2:
                return True
            color[node] = 1
            for t in d[node]:
                if not dfs(t):
                    return False
            color[node] = 2
            return True
        for t in range(numCourses):
            if color[t] == 0 and not dfs(t):
                return False
        return True















        # d = defaultdict(int)
        # for x , y in prerequisites:
        #     d[x]= y

        # def detect(val, visited):
        #     if val not in d:
        #         return True
        #     if val in visited:
        #         return False
        #     visited.add(val)
        #     if not detect(d[val], visited):
        #         return False
        #     return detect(d[val] , visited)
        # for i in range(numCourses):
        #     if not detect(i , set()):
        #         return False
        # return True
            







        # visited = set()
        # d = defaultdict(int)
        # for x , y in prerequisites:
        #     d[x]= y
        # cur = 0
        # while cur < numCourses:
        #     if cur in visited:
        #         return False
        #     if cur not in d:
        #         cur = cur + 1
        #     visited.add(cur)
        #     cur = d[cur]
        # return True










        # white , black , gray = 0 , 1 , 2
        # matches = {i : white for i in range(numCourses)}
        # values = defaultdict(list)
        # # {   1: [2,3,4],
        # #     2 : [5,6,7],
        # #     3 : [2,9,4]
        # # }
        # for x , y in prerequisites:
        #     values[x].append(y)
        # def cycleDetect(node):
        #     if matches[node] == gray:
        #         return False
        #     elif matches[node] == black:
        #         return True
        #     matches[node]= gray
        #     for t in values[node]:
        #         if not cycleDetect(t):
        #             return False
        #     matches[node] = black
        #     return True
        # for nei in range(numCourses):
        #     if matches[nei] == white:
        #         if not cycleDetect(nei):
        #             return False
        # return True

            
                
            
            
        
























        # graph = defaultdict(list)
        # gray = set()
        # # black = set()
        # for x , y in prerequisites:
        #     graph[x].append(y)
        # def cycle(node):
        #     # if node in black:
        #     #     return True
        #     if node in gray:
        #         return False
        #     gray.add(node)
        #     for t in graph[node]:
        #         if not cycle(t):
        #             return False
        #     gray.remove(node)
        #     # black.add(node)
        #     return True
        # for y in range(numCourses):
        #     if not cycle(y):
        #         return False
        # return True 





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




            






        

        
        