class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        res = []
        def iterateCurve(openn, close):
            nonlocal n
            if openn == close == n:
                res.append("".join(path))
                return
            if openn <= n:
                path.append("(")
                iterateCurve(openn + 1 , close)
                path.pop()
            if close < openn:
                path.append(")")
                iterateCurve(openn, close + 1)
                path.pop()
        iterateCurve(0 , 0)
        return res






















        # stes = ["(", ")"]
        # res = []
        # path = []
        # def iterateCurve():
        #     nonlocal n
        #     if path.count("(") == n and path.count(")") == n:
        #         stack = []
        #         for t in path:
        #             if t == "(":
        #                 stack.append(t)
        #             else:
        #                 if not stack or stack[-1] == ")":
        #                     return
        #                 stack.pop()
        #         if len(stack) == 0:
        #             res.append("".join(path))
        #         return                        
        #     if path.count("(") > n or path.count(")") > n:
        #         return
        #     for t in stes:
        #         path.append(t)
        #         iterateCurve()
        #         path.pop()
        # iterateCurve()
        # return res

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna