class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        d = defaultdict(list)
        odgree = [0 for _ in range(n +1)]
        cur_cost = [0 for i in range(n + 1)]
        for x , y in relations:
            d[x].append(y)
            odgree[y] += 1
        queue= deque()
        for i in range(1 , n + 1):
            if odgree[i] == 0:
                queue.append(i)
                cur_cost[i] = time[i - 1]
       
        while queue:
            temp = queue.popleft()
            for t in d[temp]:
                cur_cost[t] = max(cur_cost[t], cur_cost[temp] + time[t - 1])
                odgree[t] -= 1
                if odgree[t] == 0:
                    queue.append(t)
        return max(cur_cost)
            
    







        #     maxx = 0
        #     for t in range(len(queue)):
        #         temp = queue.popleft()
        #         maxx = max(maxx, time[temp - 1])
        #         for k in d[temp]:
        #             odgree[k] -= 1
        #             if odgree[k] == 0:
        #                 queue.append(k)
                
        #     total += maxx
        # return total











        # d = defaultdict(list)
        # color = [0 for _ in range(n)]
        # for x, y in relations:
        #     d[y].append(x)
        # def dfs(node):
        #     if color[node] == 1:
        #         return 
        #     res = time[node - 1]
        #     minn = float("inf")
        #     for t in d[node]:
        #         minn = min(minn, dfs(t)) 
        #     if minn== float("inf"):
        #         return res
        #     return res + minn

        





        # total = 0
        # odgree = [0 for _ in range(n)]
            # odgree[x] += 1
        # queue = deque([i for i in range(n) if odgree[i]==0])
        # while queue:
        #     temp= queue.popleft()
        #     total += time[temp - 1]
        #     for i in d[temp]:
        #         odgree



        # color = [0 for _ in range(n)]
        # for x, y in relations:
        #     d[y].append(x)
        # def dfs(node):
        #     minn = time[node]
        #     fl = float("inf")
        #     for t in d[node]:
        #         fl = min(fl, dfs(t))
        #     return minn

        

