class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visited = set()
        d = defaultdict(list)
        count = 0
        length = len(isConnected)
        for i in range(length):
            for j in range(i + 1 , length):
                if isConnected[i][j] == 1:
                    d[i].append(j)
                    d[j].append(i)
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for k in d[i]:
                dfs(k)

        for i in range(length):
            if i not in visited:
                count += 1
                dfs(i)
        return count

        # length = len(isConnected)
        # unionRep = [i for i in range(length)]
        # size = [1] * length
        # def whoConnect(a):
        #     val = a
        #     while unionRep[val] != val:
        #         val = unionRep[val]
        #     return val
        # def connectValues(a , b):
        #     itemA = whoConnect(a)
        #     itemB = whoConnect(b)
        #     if size[itemA] > size[itemB]:
        #         itemA,  itemB = itemB , itemA
        #     unionRep[itemA] = itemB
        #     size[itemB] += size[itemA]
        # for i in range(length):
        #     for j in range(i + 1, length):
        #         if isConnected[i][j] == 1:
        #             connectValues(i , j)
        # s = set()
        # for t in range(length):
        #     s.add(whoConnect(t))
        # return len(s)

        






















        # temp = defaultdict(list)
        # for i in range(len(isConnected)):
        #     for j in range(len(isConnected)):
        #         if isConnected[i][j] == 1:
        #             temp[i + 1].append(j + 1)
        # v = set()
        # op = 0
        # def trial(k):
        #     v.add(k)
        #     for i in temp[k]:
        #         if i in v:
        #             continue
        #         trial(i)    
        
        # for i in temp.keys():
        #     if i not in v:
        #         op += 1
        #         trial(i)
        # return op

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna