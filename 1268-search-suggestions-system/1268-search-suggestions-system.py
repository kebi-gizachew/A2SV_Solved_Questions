class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        d = defaultdict(list)
        res = []
        for i in products:
            for k in range(len(i)):
                d[i[:(k + 1)]].append(i)
        for y in d.values():
            y.sort()

        for i in range(len(searchWord)):
            subArray = d[searchWord[:i + 1]]
            leng = len(subArray)
            if  leng >= 3:
                leng = 3
            res.append(subArray[:leng])
        return res


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna