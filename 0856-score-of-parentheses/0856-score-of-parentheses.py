class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        count = 0
        for i in s:
            if i == "(":
                stack.append(count)
                count = 0
            elif i == ")":
                temp = stack.pop()
                count = temp + max(2* count , 1)
        return count






        # stack=[0]
        # for i in s:
        #     if i=="(":
        #         stack.append(0)
        #     else:
        #         stat=stack.pop()
        #         stack[-1]+=max(2*stat,1)
        # return stack[0]