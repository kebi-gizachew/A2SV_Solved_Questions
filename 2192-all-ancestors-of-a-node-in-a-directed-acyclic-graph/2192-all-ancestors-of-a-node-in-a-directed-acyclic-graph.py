class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ansc = defaultdict(list)
        for x , y in edges:
            ansc[y].append(x)
        ans = [[] for i in range(n)]
        def trialCycle(node, temp, vis):
            if not ansc[temp]:
                return
            for t in ansc[temp]:
                if t not in vis:
                    trialCycle(node , t, vis)
                    vis.add(t)
                    ans[node].append(t)
        for t in range(n):
            visited = set()
            trialCycle(t , t, visited)
        for k in ans:
            k.sort()
        return ans





        # queue = deque([0])
        # while queue:
        #     temp = queue.popleft()
        #     for t in ansc[temp]:
        #         ans[temp].append(t)
        #         queue.append(t)

        