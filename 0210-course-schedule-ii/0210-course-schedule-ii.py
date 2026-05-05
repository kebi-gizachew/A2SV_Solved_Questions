class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        indegree = [0] * numCourses
        for x, y in prerequisites:
            d[y].append(x)
            indegree[x]+= 1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        res = []
        while queue:
            temp = queue.popleft()
            res.append(temp)
            for t in d[temp]:
                indegree[t] -= 1
                if indegree[t] == 0:
                    queue.append(t)
        return res if len(res) == numCourses else []
    
        











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

        