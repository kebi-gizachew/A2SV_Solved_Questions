class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        res = []
        for x , y in tickets:
            heappush(d[x], y)
        def dfs(node):
            if not node:
                return
            while d[node]:
                temp = heappop(d[node])
                dfs(temp)
            res.append(node)
        dfs("JFK")
        return res[::-1]
            
















        # d = defaultdict(list)
        # for x, y in tickets:
        #     heappush(d[x], y)
        # res = []
        # def dfs(val):
        #     while d[val]:
        #         temp = heappop(d[val])
        #         dfs(temp)
        #     res.append(val)
        # dfs("JFK")
        # return res[::-1]



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna