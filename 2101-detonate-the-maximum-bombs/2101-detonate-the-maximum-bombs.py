class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        grap = [[] for i in range(len(bombs))]
        maxx = 0
        for i in range(len(bombs)):
            (x1 ,y1 , z1) = bombs[i]
            for j in range(len(bombs)):
                if i == j:
                    continue
                (x2 , y2 ,z2) = bombs[j]
                if (x1- x2) ** 2 + (y1 - y2) ** 2 <=z1**2:
                    grap[i].append(j)
        def countBombing(indx , vis):
            if indx in vis:
                return
            vis.add(indx)
            for t in grap[indx]:
                countBombing(t , vis)
        for i in range(len(grap)):
            vis = set()
            countBombing(i , vis)
            maxx = max(maxx , len(vis))
        return maxx


                














        # maxx = 0

        # def cycleBombing(xmax , ymax , xmin, ymin, nums, temp):
        #     nonlocal maxx
        #     if not nums:
        #         maxx = max(maxx , temp)
        #     for t in range(len(nums)):
        #         (x , y , radius) = nums[t]
        #         if xmin <= x - radius <= xmax and ymin <= y -radius <= ymax:
        #             cycleBombing(x + radius , y + radius, x - radius , y - radius, nums[t + 1:] + nums[:t], temp + 1)
        #         else:
        #             maxx = max(maxx , temp)
        # for t in range(len(bombs)):
        #     (x, y , z) = bombs[t]
        #     cycleBombing(x + z, y + z , x - z , y - z , bombs[t + 1:], 1)
        # return maxx













            # tempCircles = 0
            # x , y , radius = bombs[index]
            # if not (xmin <= x - radius <= xmin and ymin <= y - radius <= ymax):
            #     tempCircles += 1 + cycleBombing(x + radius, y + radius, x - radius, y -radius, index+1)
            # else:
            #     maxx = max(maxx , tempCircles)
            # return tempCircles


        