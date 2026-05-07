class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue= defaultdict(list)
        for x, y in redEdges:
            red[x].append(y)
        for x, y in blueEdges:
            blue[x].append(y)
        redd = [float("inf") for _ in range(n)]
        bluee = [float("inf") for _ in range(n)]
        redd[0] , bluee[0] = 0 , 0
        queue = deque([(0 , "red"), (0 , "blue")])
        while queue:
            for i in range(len(queue)):
                val , color = queue.popleft()
                if color == "red":
                    for t in blue[val]:
                        bluee[t] = min(bluee[t] , redd[val] + 1)
                        queue.append((t , "blue"))
                else:
                    for t in red[val]:
                        redd[t] = min(redd[t] , bluee[val] + 1)
                        queue.append((t, "red"))
        res= []
        for t in range(n):
            minn = min(redd[t] , bluee[t])
            if minn == float("inf"):
                res.append(-1)
            else:
                res.append(minn)
        return res

























        # redD = defaultdict(list)
        # blueD = defaultdict(list)
        # for x, y in redEdges:
        #     redD[x].append(y)
        # for x,y in blueEdges:
        #     blueD[x].append(y)
        # bans , rans = [float("inf")]*n , [float("inf")]*n
        # queue = deque([(0 , "r") , (0 , "b")])
        # bans[0] = rans[0] = 0
        # while queue:
        #     temp , color = queue.popleft()
        #     if color == "b":
        #         for t in redD[temp]:
        #             if bans[temp] + 1 < rans[t]:
        #                 rans[t] = bans[temp] + 1
        #                 queue.append((t , "r"))
        #     else:
        #         for t in blueD[temp]:
        #             if rans[temp] + 1 < bans[t]:
        #                 bans[t] = rans[temp] + 1
        #                 queue.append((t , "b"))
        # ans = []
        # for t in range(n):
        #     r = min(bans[t] , rans[t])
        #     if r  == float("inf"):ans.append(-1)
        #     else:
        #         ans.append(r)
        # return ans
                    



        
        
        
        
        
        
        
        
        
        
        
        
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

                    






        