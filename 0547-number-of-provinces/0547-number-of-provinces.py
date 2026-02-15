class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        temp = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    temp[i + 1].append(j + 1)
        v = set()
        op = 0
        def trial(k):
            v.add(k)
            for i in temp[k]:
                if i in v:
                    continue
                trial(i)    
        
        
        for i in temp.keys():
            if i not in v:
                op += 1
                trial(i)
        return op