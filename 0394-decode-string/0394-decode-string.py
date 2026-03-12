class Solution:
    def decodeString(self, s: str) -> str:
        st = {"]":"["}
        stack = []
        for i in s:
            if i not in st:
                stack.append(i)
            else:
                temp =""
                while stack and stack[-1] != st[i]:
                    temp = stack.pop() + temp
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num= stack.pop() + num
                stack.append(temp * int(num))
        return "".join(stack)


        