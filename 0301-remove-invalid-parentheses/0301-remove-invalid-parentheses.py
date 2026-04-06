class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = set()
        path = []
        opened , closed = 0 , 0
        for i in s:
            if i == "(":
                opened += 1
            if i == ")":
                if opened > 0:
                    opened -=1
                else:
                    closed += 1
        def trial(op , cl , left , right , index):
            if index == len(s):
                if left ==0 and right == 0:
                    res.add("".join(path[:]))
                return
            if s[index] == "(" and op >0:
                trial(op - 1, cl , left, right , index + 1)
            if s[index] == ")" and cl > 0:
                trial(op , cl - 1 , left ,right , index + 1)
            if s[index] not in "()":
                path.append(s[index])
                trial(op , cl , left , right , index + 1)
                path.pop()
            elif s[index] == "(":
                path.append(s[index])
                trial(op , cl , left + 1 , right , index + 1)
                path.pop()
            elif s[index] == ")" and left > 0:
                path.append(s[index])
                trial(op , cl , left -1 , right , index + 1)
                path.pop()
        trial(opened, closed , 0 , 0 , 0)
        return list(res)
        










        # path = []
        # res = []
        # def trial(st):
        #     if not st:
        #         stack = []
        #         for t in path:
        #             if t == "(":
        #                 stack.append("(")
        #             elif t == ")":
        #                 if not stack:
        #                     return
        #                 else:
        #                     stack.pop()
        #         if not stack:
        #             res.append("".join(path[:]))
        #         return
        #     for i in range(len(st)):
        #         path.append(st[i])
        #         trial(st[i + 1:])
        #         path.pop()
        # trial(s)
        # return res
        
