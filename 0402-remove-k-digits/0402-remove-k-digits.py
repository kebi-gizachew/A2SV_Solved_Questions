class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        drop= k
        stack = []
        for i in range(len(num)):
            while drop and stack and int(stack[-1]) > int(num[i]):
                stack.pop()
                drop -= 1
            if not stack and num[i] == "0":
                continue
            stack.append(num[i])
        stack = stack[:(len(stack) - drop)]

        return "".join(stack) if stack else "0"
        