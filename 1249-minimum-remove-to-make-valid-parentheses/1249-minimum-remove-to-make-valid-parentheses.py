class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        last_set = set()
        for i , j in enumerate(s):
            if j == "(":
                stack.append(i)
            elif j ==")":
                if stack:
                    stack.pop()
                else:
                    last_set.add(i)
        last_set = last_set.union(set(stack))
        final = []
        for y in range(len(s)):
            if y not in last_set:
                final.append(s[y])
        return "".join(final)
