class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = defaultdict(list)
        i = 0
        path = []
        res = []
        for j in range(2 , 10):
            if j != 7 and j != 9:
                for k in range(i , 3 + i):
                    temp = chr(ord("a") + k)
                    d[str(j)].append(temp)
                i += 3
            else:
                for k in range(i, i + 4):
                    temp = chr(ord("a") + k)
                    d[str(j)].append(temp)
                i += 4
        # print(d)
        def backtrack(val):
            if val >= len(digits):
                res.append("".join(path))
                return
            for t in d[digits[val]]:
                path.append(t)
                backtrack(val + 1)
                path.pop()
        backtrack(0)
        return res



            
            
















        # arr = [[] for i in range(10)]
        # path = []
        # res = []
        # num = 97
        # for i in arr[2:]:
        #     i.append(chr(num))
        #     i.append(chr(num + 1))
        #     i.append(chr(num + 2))
        #     if i[-1] == "r" or i[-1] == "y":
        #         i.append(chr(num + 3))
        #         num += 4
        #         continue
        #     num += 3
        # print(arr)
        # def finite(i):
        #     if len(digits) == i:
        #         res.append("".join(path[:]))
        #         return

        #     for k in arr[int(digits[i])]:
        #         path.append(k)
        #         finite(i + 1)
        #         path.pop()
        #     return
        # finite(0)
        # return res




            









        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna