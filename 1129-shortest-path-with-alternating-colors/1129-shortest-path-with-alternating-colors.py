class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redD = defaultdict(list)
        blueD = defaultdict(list)
        for x, y in redEdges:
            redD[x].append(y)
        for x,y in blueEdges:
            blueD[x].append(y)
        bans , rans = [float("inf")]*n , [float("inf")]*n
        queue = deque([(0 , "r") , (0 , "b")])
        bans[0] = rans[0] = 0
        while queue:
            temp , color = queue.popleft()
            if color == "b":
                for t in redD[temp]:
                    if bans[temp] + 1 < rans[t]:
                        rans[t] = bans[temp] + 1
                        queue.append((t , "r"))
            else:
                for t in blueD[temp]:
                    if rans[temp] + 1 < bans[t]:
                        bans[t] = rans[temp] + 1
                        queue.append((t , "b"))
        ans = []
        for t in range(n):
            r = min(bans[t] , rans[t])
            if r  == float("inf"):ans.append(-1)
            else:
                ans.append(r)
        return ans
                    



        
        
        
        
        
        
        
        
        
        
        
        
        # redD = defaultdict(list)
        # blueD = defaultdict(list)
        # queue = deque([0])
        # res = []
        # for x , y in redEdges:
        #     redD[x].append(y)
        # for x, y in blueEdges:
        #     blueEdges[x].append(y)
        # flag = True
        # while queue:
        #     for t in queue:
        #         temp = queue.popleft()
        #         if not res:
        #             if temp in redD or temp in blueD:
        #                 res.append(temp)
        #             else:
        #                 res.append(-1)
        #         else:
        #             if flag:
        #                 if temp in redD[temp]:
        #                     res.append(temp)
        #                 else:
        #                     res.append(temp)
        #             else:
        #                 if temp in blueD:
        #                     res.append(temp)
        #                 else:
        #                     res.append(-1)

                    






        