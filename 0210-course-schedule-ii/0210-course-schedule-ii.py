class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        color = [0 for _ in range(numCourses)]
        res = []
        for x, y in prerequisites:
            d[y].append(x)
        def dfs(node):
            if color[node] == 1:
                return False
            if color[node] == 2:
                return True
            color[node] = 1
            for i in d[node]:
                if not dfs(i):
                    return False
            res.append(node)
            color[node] = 2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res[::-1]

        



        # color = [0 for i in range(numCourses)]
        # d= defaultdict(list)
        # res = []
        # for x, y in prerequisites:
        #     d[y].append(x)
        # def dfs(node):
        #     if color[node] == 1:
        #         return False
        #     if color[node] == 2:
        #         return True
        #     color[node] = 1
        #     for k in d[node]:
        #         if not dfs(k):
        #             return False
        #     res.append(node)
        #     color[node] = 2
        #     return True
        # for num in range(numCourses):
        #     if color[num] == 0 and not dfs(num):
        #         return []
        # return res[::-1]




        # d = defaultdict(list)
        # indegree = [0] * numCourses
        # for x, y in prerequisites:
        #     d[y].append(x)
        #     indegree[x]+= 1
        # queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        # res = []
        # while queue:
        #     temp = queue.popleft()
        #     res.append(temp)
        #     for t in d[temp]:
        #         indegree[t] -= 1
        #         if indegree[t] == 0:
        #             queue.append(t)
        # return res if len(res) == numCourses else []
        # it is going to be empty if there is a cycle becuause at some point where the whole indgreee is notzero and the queue is empty it will return res before fully iterating
    
        











        # d = defaultdict(list)
        # res = set()
        # for x, y in prerequisites:
        #     d[x].append(y)
        # def detect(val, visited):
        #     if val in visited:
        #         return False
        #     if val not in d:
        #         return True
        #     visited.add(val)
        #     for t in d[val]:
        #         res.add(t)
        #         if not detect(t, visited):
        #             return False
        #     res.add(val)

        #     return True
        # for i in range(numCourses):
        #     if not detect(i, set()):
        #         return []
        # return list(res)

        